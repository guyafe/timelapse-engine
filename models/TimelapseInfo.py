class TimelapseInfo:
    def __init__(self, satellite, polygon):
        self.satellite = satellite
        self.polygon = polygon

    def __str__(self):
        return f"satellite: {self.satellite}; polygon: {self.polygon}"
