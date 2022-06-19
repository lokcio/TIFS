import os

from Model.Task import Task
from Service.BasicAnalyzeService import BasicAnalyzeService
from container import container
import gzip

basic_analyze_service = container[BasicAnalyzeService]

class EXPORTProvider:
    def __init__(self, task: Task):
        self.task = task

    def save_file(self):
        sources = self.task.params.get('source_blacklists_names')
        data = basic_analyze_service.gen_blacklist_file(sources)
        filename = "./blacklists/" +self.task.params.get('file_name')
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(data)

        with open(filename, 'rb') as src, gzip.open(filename+".gz", 'wb') as dst:
            dst.writelines(src)
        self.data = ""
        return True
