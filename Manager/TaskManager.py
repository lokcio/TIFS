from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

from Model.Task import Task


class TaskManager:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def insert_one(self, task: Task):
        self.db.session.add(task)
        self.db.session.commit()
        return True

    def insert_many(self, tasks: list):
        for task in tasks:
            self.db.session.add(task)
        self.db.session.commit()
        return True

    def update_one(self, task: Task):
        self.db.session.merge(task)
        self.db.session.commit()
        return True

    def find_all(self):
        return self.db.session.query(Task).all()

    def truncate(self):
        return self.db.session.query(Task).delete()
