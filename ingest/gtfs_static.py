"""
GTFS Static ingestion script.
Downloads the GTFS Sweden 3 zip from Trafiklab and loads CSVs into Postgres raw schema.
"""

import requests
import os
import sys
import zipfile
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

load_dotenv()

api_key = os.environ.get("TRAFIKLAB_GTFS_STATIC_KEY")
if not api_key:
    print("ERROR: TRAFIKLAB_GTFS_STATIC_KEY not found in .env")
    sys.exit(1)

# We print the length instead of the actual key so we can confirm it loaded without exposing the secret in the terminal output.

print(f"API key loaded ({len(api_key)} characters)")

# Full Sweden feed - we filter to SL operator later in dbt, not here.
# Keeping all of Sweden in raw means we can add other cities without re-downloading.

url = f"https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip?key={api_key}"
zip_path = "data/gtfs-sweden.zip"

print("Downloading GTFS zip...")

# Trafiklab requires Accept-Encoding header — without it, returns a JSON error instead of the zip.

response = requests.get(url, headers={"Accept-Encoding": "gzip, deflate"}, timeout=120)

if response.status_code != 200:
    print(f"ERROR: Download failed with status {response.status_code}")
    sys.exit(1)

# Binary write — zip files are not text

with open(zip_path, "wb") as f:
    f.write(response.content)

size_mb = len(response.content) / 1024 / 1024
print(f"Downloaded {size_mb:.1f} MB to {zip_path}")

# Unzip to data/gtfs-sweden/, overwriting any previous extract

extract_dir = "data/gtfs-sweden"
print(f"Extracting to {extract_dir}/...")
with zipfile.ZipFile(zip_path, "r") as z:
    z.extractall(extract_dir)

print(f"Extracted {len(os.listdir(extract_dir))} files")

# Load CSVs into Postgres
# The format of the  connection string: postgresql://username:password@host:port/database

db_url = f"postgresql://dwh_admin:{quote_plus(os.environ.get('POSTGRES_PASSWORD'))}@localhost:5432/dwh"
engine = create_engine(db_url)

# Tier 1: small files to test with

tier1_files = ["agency.txt", "routes.txt", "calendar.txt", "feed_info.txt"]

for filename in tier1_files:
    table_name = filename.replace(".txt", "")
    filepath = f"{extract_dir}/{filename}"
    print(f"Loading {filename} into raw.{table_name}...")
    df = pd.read_csv(filepath)
    df.to_sql(table_name, engine, schema="raw", if_exists="replace", index=False)
    print(f"  → {len(df)} rows loaded")

# Tier 2: medium files
tier2_files = ["stops.txt", "trips.txt", "calendar_dates.txt"]

for filename in tier2_files:
    table_name = filename.replace(".txt", "")
    filepath = f"{extract_dir}/{filename}"
    print(f"Loading {filename} into raw.{table_name}...")
    df = pd.read_csv(filepath)
    df.to_sql(table_name, engine, schema="raw", if_exists="replace", index=False)
    print(f"  → {len(df)} rows loaded")


