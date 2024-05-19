from time import strptime


class TimelapseInfo:
    def __init__(self, satellite, polygon, start, end):
        self.satellite = satellite
        self.polygon = polygon
        self.start = strptime(start, "%Y-%m-%d")
        self.end = strptime(end, "%Y-%m-%d")

    def __str__(self):
        return f"satellite: {self.satellite}; polygon: {self.polygon}; start: {self.start}; end: {self.end}"
