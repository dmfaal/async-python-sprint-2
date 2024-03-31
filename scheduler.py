import copy
import inspect
import json
import pickle
from collections import deque
from dataclasses import dataclass
from datetime import datetime
from multiprocessing import Process
from threading import Thread, Timer
from logger.logger import my_logs
from job import Job, Status

logger = my_logs()
STATUS_FILE = 'scheduler_status.json'


@dataclass
class Task:
    pass


class Scheduler:
    def __init__(self, pool_size: int = 10, tasks: list[Task] | None = None):
        self.tasks = tasks or []
        self.pool_size = pool_size
        self.sleeping_tasks = deque()

    def schedule(self, task):
        pass

    def run(self):
        pass

    def restart(self):
        pass

    def stop(self):
        pass