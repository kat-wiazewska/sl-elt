#!/bin/bash

# SL-ELT pipeline: ingest GTFS static data, then run dbt transformations
set -e

# Step 1: Ingest GTFS static data
cd ~/sl-elt

source venv/bin/activate
python ingest/gtfs_static.py
deactivate

# Step 2: Run dbt transformations
source ~/dbt-env/bin/activate
cd ~/sl-elt/dbt
dbt run
deactivate

echo "Pipeline completed successfully at $(date)"
