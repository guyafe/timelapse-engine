class Polygon:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        rv = ""
        for coordinate in self.coordinates:
            rv += coordinate
        return rv
