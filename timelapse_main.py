import json
import sys

import ee

from models.TimelapseInfo import TimelapseInfo


def main():
    print("Starting timelapse engine...")
    ee.Authenticate()
    ee.Initialize(project='timelapse-sample')
    timelapse_info = load_timelapse_info()


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
