import logging
log = logging.getLogger(__name__)
print(log)

class Match:
    def __init__(self):
        self.extern = None
        self.host = None
        self.distance = None
        self.match_score = None

    def set_extern(self, extern):
        self.extern = extern

    def set_host(self, host):
        self.host = host

    def set_distance(self, distance):
        self.distance = int(distance)

    def set_match_score(self, match_score):
        self.match_score = match_score
    def __str__(self):
        return f"Extern {self.extern.name} is {self.distance} km from host {self.host.name} : with a match score of {self.extern + self.host}"