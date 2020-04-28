#!/usr/bin/env python3

"""Script to get the data"""

import requests
import pandas as pd
import os


def main():

    mkdir()
    get_beecolonyloss_data()
    get_pesticide_data()


def mkdir():
    already_exist = False
    dirName = 'data'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        already_exist = True
        print("Directory ", dirName, " already exists")


def get_beecolonyloss_data():
    bee_data_url = "https://query.data.world/s/ddqzkn5frwwo5cn53hyindd32hy6lv"
    bee_DataSet = requests.get(bee_data_url)
    with open('data/bee_colony_loss.xlsx', 'wb') as fid:
                 fid.write(bee_DataSet.content)


def get_pesticide_data():
    pesticide_use_2013_url = "https://water.usgs.gov/nawqa/pnsp/usage/maps/county-level/PreliminaryEstimates/EPest.county.estimates.2013.txt"
    pesticide_use_2014_url = "https://water.usgs.gov/nawqa/pnsp/usage/maps/county-level/PreliminaryEstimates/EPest.county.estimates.2014.txt"

    pesticide_use_2013_dataset = requests.get(pesticide_use_2013_url)
    pesticide_use_2014_dataset = requests.get(pesticide_use_2014_url)

    with open('data/pesticide_use_2013_dataset.txt', 'wb') as fid:
                 fid.write(pesticide_use_2013_dataset.content)
    with open('data/pesticide_use_2014_dataset.txt', 'wb') as fid:
                 fid.write(pesticide_use_2014_dataset.content)

    #datasets of 2015 and 2016 are packed in a zip file. Text files will be saved under data directory.
    import zipfile, io
    pesticide_use_2015_url = "https://water.usgs.gov/nawqa/pnsp/usage/maps/county-level/PreliminaryEstimates/2015PreliminaryEstimates.zip"
    pesticide_use_2015_request = requests.get(pesticide_use_2015_url)
    z1 = zipfile.ZipFile(io.BytesIO(pesticide_use_2015_request.content))
    z1.extractall('data/')

    pesticide_use_2016_url = "https://water.usgs.gov/nawqa/pnsp/usage/maps/county-level/PreliminaryEstimates/2016PreliminaryEstimates.zip"
    pesticide_use_2016_request = requests.get(pesticide_use_2016_url)
    z2 = zipfile.ZipFile(io.BytesIO(pesticide_use_2016_request.content))
    z2.extractall('data/')


if __name__ == '__main__':
    main()
    print("Successfully fetched data")
    
