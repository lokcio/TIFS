from sqlalchemy.orm import Session

from Model.Blacklist import Blacklist


class BlacklistManager:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def insert_one(self, blacklist: Blacklist):
        self.db.session.add(blacklist)
        self.db.session.commit()
        return True

    def insert_many(self, blacklists: list):
        for blacklist in blacklists:
            self.db.session.add(blacklist)
        self.db.session.commit()
        return True

    #
    # def findOneByUniqueId(self, uniqueId: str):
    #     return self.findOne({'uniqueId': uniqueId})
    #
    # def findOne(self, criteria=None):
    #     if criteria is None:
    #         criteria = {}
    #     try:
    #         offerData = self.collection.find_one(criteria)
    #         return (Offer()).fromDict(offerData)
    #     except Exception as e:
    #         return None
    #
    # def find(self, criteria=None):
    #     if criteria is None:
    #         criteria = {}
    #     try:
    #         cursor = self.collection.find(criteria)
    #         return [(Offer()).fromDict(offerData) for offerData in cursor]
    #     except Exception as e:
    #         return []
    #
    # def findAll(self):
    #     return self.find({})