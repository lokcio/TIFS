from Manager.BlacklistManager import BlacklistManager
from Model.Blacklist import Blacklist
from Model.Task import Task


class BasicAnalyzeService:
    def __init__(self, blacklist_manager: BlacklistManager):
        self.blacklist_manager = blacklist_manager

    def process_task(self, task: Task):
        blacklist = Blacklist(addr="10.0.0.0/25",source="abuse.ch")
        self.blacklist_manager.insert_one(blacklist)
