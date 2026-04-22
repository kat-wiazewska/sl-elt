"""
Connectivity check for Trafiklab API keys.
"""

import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

static_key = os.environ.get("TRAFIKLAB_GTFS_STATIC_KEY")
rt_key = os.environ.get("TRAFIKLAB_GTFS_RT_KEY")

if not static_key:
   print("ERROR: TRAFIKLAB_GTFS_STATIC_KEY not found in .env")
   sys.exit(1)

if not rt_key:
   print("ERROR: TRAFIKLAB_GTFS_RT_KEY not found in .env")
   sys.exit(1)

print("Both API keys loaded from .env")

print("Testing GTFS Sweden 3 Static...")
url = f"https://opendata.samtrafiken.se/gtfs-sweden/sweden.zip?key={static_key}"
response = requests.head(url, timeout=10)

if response.status_code == 200:
   size = response.headers.get("Content-Length", "unknown")
   print(f"  OK — status {response.status_code}, file size: {size} bytes")
else:
   print(f"  FAILED — status {response.status_code}")

print("\nTesting GTFS Sweden 3 Realtime...")
url = f"https://opendata.samtrafiken.se/gtfs-rt-sweden/sl/TripUpdatesSweden.pb?key={rt_key}"
response = requests.head(url, timeout=10)

if response.status_code == 200:
    print(f"  OK — status {response.status_code}")
else:
    print(f"  FAILED — status {response.status_code}")

print("\nDone!")
