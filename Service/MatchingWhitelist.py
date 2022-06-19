import os
import ipaddress


class MatchingWhitelist:
    def __init__(self):
        self.whitelist = os.getenv('WHITELIST').split(",")

    def match_whitelist(self, x):
        black = ipaddress.ip_network(str(x))
        for white in self.whitelist:
            if ipaddress.ip_network(white).overlaps(black):
                return True
        return False
