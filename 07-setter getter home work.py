class Bus():
    min_p = 0
    max_p = 20
    _places=0
    @property
    def places(self):
        return self.places
    @places.setter
    def places(self):
        if places <0:
            self.places =0
        if places >20:
            self.places =20
        return self.places = places
        bus = Bus()
bus.places = -2
print(bus.places)