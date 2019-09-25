# CPE 202 Lab 0

# represents a location using name, latitude and longitude
class Location:

    def __init__(self, name, lat, lon):
        self.name = name    # string for name of location
        self.lat = lat      # latitude in degrees (-90 to 90)
        self.lon = lon      # longitude in degrees (-180 to 180)

    def __eq__(self, other):
        return isinstance(other, Location) and self.name == other.name and self.lat == other.lat and self.lon == other.lon

    def __repr__(self):
        return f"Location({repr(self.name)}, {self.lat}, {self.lon})"
