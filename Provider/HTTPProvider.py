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
            if line == '':
                continue
            if "#" in line:
                if "#" != line[0]:
                    line = line[:line.find("#")]
                else:
                    continue
            if " " in line:
                line = line.replace(" ", "")
            data.append(Blacklist(addr=line, source=self.task.name))
        return data
