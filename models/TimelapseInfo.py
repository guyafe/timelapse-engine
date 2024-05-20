class TimelapseInfo:
    def __init__(self, satellite, geo_json, start: str, end: str, max_pixel_value, rgb_bands, dimensions, folder, file_prefix, description, frames_per_second):
        self.satellite = satellite
        self.geo_json = geo_json
        self.start = start
        self.end = end
        self.max_pixel_value = max_pixel_value
        self.rgb_bands = rgb_bands
        self.dimensions = dimensions
        self.folder = folder
        self.file_prefix = file_prefix
        self.description = description
        self.frames_per_second = frames_per_second

