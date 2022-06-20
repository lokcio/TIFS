from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date

from Manager.BlacklistManager import BlacklistManager
from Manager.TaskManager import TaskManager
from Model.Task import Task
from Provider.EXPORTProvider import EXPORTProvider
from Provider.HTTPProvider import HTTPProvider
from container import container
import time

blacklistManager = container[BlacklistManager]
taskManager = container[TaskManager]


def create_provider_by_type(task: Task):
    if task.provider == 'HTTP':
        return HTTPProvider(task)
    elif task.provider == 'EXPORT':
        return EXPORTProvider(task)


def execute_task(task: Task):
    if task.provider == 'EXPORT':
        provider = create_provider_by_type(task)
        provider.save_file()

    else:
        blacklistManager.delete_by_task_name(task.name)
        provider = create_provider_by_type(task)
        data = provider.get_data()
        blacklistManager.insert_many(data)
        task.last_run = date.today()
        task.last_result = "SUCCESS"
        taskManager.update_one(task)


class TaskRunnerService:
    def __init__(self, scheduler: BackgroundScheduler, taskManager: TaskManager):
        self.scheduler = scheduler
        self.taskManger = taskManager

    def start_tasks(self):
        for task in self.taskManger.find_all():
            execute_task(task)
            time.sleep(2.4)
            self.scheduler.add_job(execute_task, 'interval', minutes=task.interval, id=task.name, kwargs={'task': task})
        self.scheduler.start()
