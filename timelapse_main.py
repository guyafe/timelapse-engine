import json
import sys

import ee

from models.TimelapseInfo import TimelapseInfo


def main():
    print("Starting timelapse engine...")
    ee.Authenticate()
    ee.Initialize(project='timelapse-sample')
    timelapse_info = load_timelapse_info()
    build_timelapse_animation(timelapse_info)


def build_timelapse_animation(timelapse_info):
    print(f"Building timelapse animation from satellite: {timelapse_info.satellite}")
    satellite_collection = ee.ImageCollection(timelapse_info.satellite)


def load_timelapse_info():
    timelapse_info_path = sys.argv[1]
    print(f"Loading timelapse_info from: {timelapse_info_path}")
    timelapse_info_file = open(timelapse_info_path, "r")
    timelapse_info_data = json.load(timelapse_info_file)
    timelapse_info = TimelapseInfo(**timelapse_info_data)
    print(f"Loaded timelapse_info_data: {timelapse_info}")
    return timelapse_info


if __name__ == "__main__":
    main()
