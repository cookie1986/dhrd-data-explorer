import pandas as pd
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from dhrd_data_explorer.data.load import load_data

data = load_data()

incident_data = data[1]

# Standardise names to prevent mismatches
name_fixes = {
    "East":"East",
    "North West":"North West (England)",
    "East Midlands":"East Midlands (England)",
    "North East":"North East (England)",
    "Greater London":"London",
    "South East":"South East (England)",
    "South West":"South West (England)",
    "Yorkshire and Humber":"Yorkshire and The Humber",
    "West Midlands":"West Midlands (England)",
    "Wales":"Wales"
}
incident_data['region'] = incident_data['region'].replace(name_fixes)

incident_data.to_csv('dataset/02_incidents.csv', index=False)