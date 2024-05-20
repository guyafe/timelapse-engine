import json
import sys

import ee
from ee.batch import Export

from models.TimelapseInfo import TimelapseInfo


def main():
    print("Starting timelapse engine...")
    ee.Authenticate()
    ee.Initialize(project='timelapse-sample')
    timelapse_info = load_timelapse_info()
    build_timelapse_animation(timelapse_info)


def convert_bit(image, max_pixel_value):
    return image.divide(max_pixel_value).multiply(2 << 8).uint8()


def build_timelapse_animation(timelapse_info):
    print(f"Building timelapse animation from satellite: {timelapse_info.satellite}")
    satellite_collection = (ee.ImageCollection(timelapse_info.satellite)
                            .filterDate(ee.DateRange(timelapse_info.start, timelapse_info.end))  # Filter by date
                            .filterBounds(timelapse_info.geo_json)  # Filter by location
                            .select(timelapse_info.rgb_bands)  # Select RGB bands
                            .map(lambda image: convert_bit(image, timelapse_info.max_pixel_value)))  # Convert to 8-bit
    print("Exporting timelapse animation to Google Drive...")
    out = Export.video.toDrive(satellite_collection, description='timelapse', maxFrames=10000, dimensions=720,
                               framesPerSecond=2, folder="timelapse", fileNamePrefix="timelapse", maxPixels=1e12)
    out.start()
    out.active()
    print("Timelapse animation has been exported to Google Drive")


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
