"""This script is built to retrieve solar radiation from sonnendach.ch
   For that, we use the API from the Swiss confederation using multiple queries. First, we use the coordinates
   on a address to get a building_id, with this building_id we identify all roofs linked to this building and
   retrieve solar radiation and electricity production as well as surface of all the roofs of a building"""

import requests
import json
import pandas as pd
import numpy as np
import time
from datetime import datetime
from pathlib import Path

# Set this path to wherever your workbook/dataset is stored
path = "C:/Users/bregy/DataScience/Data2Dollar/Gruppenarbeit/"

# Read in the dataset with pandas
df = pd.read_csv(path + "daten_brugg.csv")
"""The dataset consists of all addresses from the "Gemeinde" that we identified as most promising for solar
    panel installation. All addresses contain coordinates which we use to retrieve the solar data. In case the 
    coordinates do not yield any results, we built a second script (see solar_script_2) that makes one more request
    to the API to get the coordinates from a given address."""

# Add an empty column building_id
df["building_id"] = np.nan


# Iterate over all rows (addresses) of dataset
for index, row in df.iterrows():
    # Set coordinates of address to make a unique API request for a given address
    ADR_EASTING = row["ADR_EASTING"]
    ADR_NORTHING = row["ADR_NORTHING"]
    # Build the API request to send to the server
    API_building_ID = ('https://api3.geo.admin.ch//rest/services/api/MapServer/'
                        'identify?geometryType=esriGeometryPoint&returnGeometry=true&'
                        'layers=all:ch.bfe.solarenergie-eignung-daecher'
                        '&geometry=' + str(ADR_EASTING) + ',' + str(ADR_NORTHING) +
                        '&tolerance=0&order=distance&lang=de&sr=2056'
                       )
    # Make the request to the API using requests library
    result_building = requests.get(API_building_ID)
    # Transform result into json format
    result_building_json = result_building.json()

    # Try extracting building_id from request from json result
    try:
        building_id = result_building_json["results"][0]["attributes"]["building_id"]
        print("BuildingID: " + str(building_id))
        # Set building_id into dataframe
        df.at[index, "building_id"] = building_id
    # If building_id does not yield any results, set building_id to NaN and continue
    except KeyError:
        df.at[index, "building_id"] = np.nan
        print("No building ID found")
        continue

    # If building_id was found, make a second request to the API to get the data of roofs
    API_solar = ('https://api3.geo.admin.ch//rest/services/api/MapServer/'
                'find?layer=ch.bfe.solarenergie-eignung-daecher'
                '&searchField=building_id&searchText=' + str(building_id) + '&contains=false')

    # Make the request to the API with requests library
    result_solar = requests.get(API_solar)
    # Transform the results into json format
    result_solar_json = result_solar.json()
    # Make a list of all the roofs yielded from API request
    list_roof = result_solar_json["results"]

    # Iterate through all the roofs to extract solar data
    for i, roof in enumerate(list_roof):
        # Try extracting featureID, surface, radiation, suitability and solar yield from roof
        try:
            featureId = roof["featureId"]
            print("FeatureID: " + str(featureId))
            flaeche = roof["attributes"]["flaeche"]
            g_strahlung = roof["attributes"]["gstrahlung"]
            eignung = roof["attributes"]["klasse_text"]
            stromertrag = roof["attributes"]["stromertrag"]
        # If the roof does not have all of the attributes needed, continue
        except KeyError:
            continue

        # Set the results into the dataframe, using a count of roofs to separate the roofs from each other
        df.at[index, "dach" + str(i) + "_featureId"] = featureId
        df.at[index, "dach" + str(i) + "_flaeche"] = flaeche
        df.at[index, "dach" + str(i) + "_gstrahlung"] = g_strahlung
        df.at[index, "dach" + str(i) + "_eignung"] = eignung
        df.at[index, "dach" + str(i) + "_stromertrag"] = stromertrag

    # Export a copy of the dataframe after each 5 iterations to make sure to loose no data if the program fails
    if index % 5 == 0:
        df.to_csv(Path("results", f'brugg_{datetime.now().strftime("%m-%d_%H-%M-%S")}.csv'))

    # Make the program wait for six seconds to avoid overrunning the API that has set a limit to 20 requests/min
    time.sleep(6)

# Export a final copy of the results once all the addresses have been iterated over
df.to_csv(Path("results", 'brugg_final_results.csv'))





