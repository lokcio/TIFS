import os
import yaml
from flask_sqlalchemy import SQLAlchemy

from Manager.TaskManager import TaskManager
from Model.Task import Task


class StartupService:
    def __init__(self, taskManager: TaskManager, db: SQLAlchemy):
        self.taskManager = taskManager
        self.db = db

    def prepare_database(self):
        self.db.create_all()
        self.db.session.commit()

    def load_configuration(self, filename=os.getenv('CONFIG_NAME')):
        tasks = []
        self.taskManager.truncate()
        with open(os.getcwd() + '/' + filename) as file:
            parsed_config = yaml.safe_load(file)
            for task_name, task_config in parsed_config['tasks'].items():
                tasks.append(Task(
                    name=task_name,
                    params=task_config['params'],
                    provider=task_config['provider'],
                    interval=task_config['interval'],
                    enabled=task_config['enabled'],
                ))

        self.taskManager.insert_many(tasks)