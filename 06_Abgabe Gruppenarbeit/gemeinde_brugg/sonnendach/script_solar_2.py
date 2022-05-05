""" This second script was built to deal with missing results from lack of precision of certain address
    coordinates when running script_solar. This script makes an additional request to the API to make sure
    that an address yields the correct coordinates. It makes one more request to the API than the initial
    script."""
import math
import requests
import pandas as pd
import numpy as np
import time
from datetime import datetime
from pathlib import Path

# Set this path to wherever your workbook/dataset is stored
path = "C:/Users/bregy/DataScience/Data2Dollar/Gruppenarbeit/"

# Read in the dataset with pandas, in that case the result from running the first script
df = pd.read_csv(path + "daten_brugg_intermediate.csv", sep=";")
# Create a new column that concatenates the address fields into one to make a request from the API
df["address"] = df["STN_LABEL"] + " " + df["ADR_NUMBER"] + " " + df["ZIP_LABEL"]
# Replace all spaces in the address column by %20, the URL encoding of a space
df["address"] = df["address"].str.replace(' ', "%20")

# Iterate over all rows (addresses) of dataset
for index, row in df.iterrows():
    """If the building_id is already present, the request from script_solar was successful and hence no further action
       is needed. We can just continue"""
    if not math.isnan(row["building_id"]):
        continue

    # Make the loop wait for 9 seconds to avoid overrunning the API server and respecting the 20 requests/min
    time.sleep(9)

    # Set the address for the API request to the address from the given row
    address = row["address"]

    # Build the API request URL with the given address
    API_address = ('https://api3.geo.admin.ch//rest/services/api/SearchServer?'
                   'lang=de&searchText=' + address + '&type=locations&sr=2056')

    # Make the request on the API with requests library
    result_address = requests.get(API_address)
    # Transform result into json format
    result_address_json = result_address.json()

    # Try extracting the coordinates of the address from json
    try:
        ADR_EASTING = result_address_json["results"][0]["attrs"]["y"]
        ADR_NORTHING = result_address_json["results"][0]["attrs"]["x"]
    # If there is a key error, it means that the request yielded a result, but no coordinates
    except KeyError:
        print("No coordinates found")
        df.at[index, "building_id"] = "No coordinates found"
        continue
    # If there is an index error, it means that the request yielded no results, hence no coordinates
    except IndexError:
        print("No coordinates found")
        df.at[index, "building_id"] = "No coordinates found"
        continue

    # Build the request similar to script_solar only with new coordinates from previous request
    API_building_ID = ('https://api3.geo.admin.ch//rest/services/api/MapServer/identify'
                       '?geometryType=esriGeometryPoint&returnGeometry=true'
                       '&layers=all:ch.bfe.solarenergie-eignung-daecher'
                       '&geometry=' + str(ADR_EASTING) + ',' + str(ADR_NORTHING) +
                       '&tolerance=0&order=distance&lang=de&sr=2056')

    # Make the request to the API using requests library
    result_building = requests.get(API_building_ID)

    # Transform result into json format
    result_building_json = result_building.json()

    # Try similar approach like in script_solar
    try:
        building_id = result_building_json["results"][0]["attributes"]["building_id"]
        print("BuildingID: " + str(building_id))
        df.at[index, "building_id"] = building_id
    except KeyError:
        df.at[index, "building_id"] = "No building ID found"
        print("No building ID found")
        continue

    # If building_id was found, make a third request to the API to get the data of roofs
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

    # Export intermediate result to avoid losing data if the program fails
    df.to_csv(Path("results", f'brugg_{datetime.now().strftime("%m-%d_%H-%M-%S")}.csv'))

# Export a final copy of the results once all the addresses have been iterated over
df.to_csv(Path("results", 'results_brugg_solar_final.csv'))



