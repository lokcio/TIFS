import requests

from Model.Blacklist import Blacklist
from Model.Task import Task


class HTTPProvider:
    def __init__(self, task: Task):
        self.task = task

    def get_data(self):
        data = []
        response = requests.get(self.task.params.url)
        for line in response.text.split('/n'):
            line = line.strip()
            data.append(Blacklist(addr=line, source=self.task.name))
        return data
