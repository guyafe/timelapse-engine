class Coordinate2D:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return f"[latitude: {self.lat}; longitude:{self.lng}] "
