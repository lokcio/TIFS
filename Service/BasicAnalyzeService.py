from Manager.BlacklistManager import BlacklistManager
from Service.MatchingWhitelist import MatchingWhitelist
from netaddr import IPNetwork, cidr_merge
import time

def remove_duplicate(t):
    return list(dict.fromkeys(t))


class BasicAnalyzeService:
    def __init__(self, blacklist_manager: BlacklistManager, whitelist: MatchingWhitelist):
        self.blacklist_manager = blacklist_manager
        self.analizedAddress = list()
        self.whitelist = whitelist
        self.blacklistToFile = ""

    def process_task(self, sources):
        self.analizedAddress.clear()
        self.blacklists = self.blacklist_manager.get_all()
        for blacklistRow in self.blacklists:
            if blacklistRow.source in sources:
                self.analizedAddress.append(IPNetwork(blacklistRow.addr))
        self.analizedAddress = remove_duplicate(self.analizedAddress)
        self.analizedAddress = cidr_merge(self.analizedAddress)
        self.analizedAddress = sorted(self.analizedAddress)

    def gen_blacklist_file(self, sources):
        self.analizedAddress.clear()
        self.process_task(sources)
        for address in self.analizedAddress:
            if self.whitelist.match_whitelist(address):
                self.analizedAddress.remove(address)

        for row in self.analizedAddress:
            self.blacklistToFile += str(row) + "\n"
        self.analizedAddress.clear()
        return self.blacklistToFile
