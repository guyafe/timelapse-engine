class TimelapseInfo:
    def __init__(self, satellite, geo_json, start: str, end: str, max_pixel_value, rgb_bands):
        self.satellite = satellite
        self.geo_json = geo_json
        self.start = start
        self.end = end
        self.max_pixel_value = max_pixel_value
        self.rgb_bands = rgb_bands

    def __str__(self):
        return f"satellite: {self.satellite}; geo_json: {self.geo_json}; start: {self.start}; end: {self.end}"
