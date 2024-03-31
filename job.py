from enum import Enum
from typing import Callable, Optional, List
from datetime import datetime
from logger.logger import my_logs


class Status(str, Enum):
    STARTED = 'STARTED'
    FINISHED = 'FINISHED'
    PENDING = 'PENDING'
    FAILED = 'FAILED'


logger = my_logs()


class Job:
    def __init__(
            self,
            name,
            status,
            func,
            tries,
            kwargs


    ):
        self.kwargs = kwargs
        self.name = name
        self.status = status
        self.func = func
        self.tries = tries

    def run(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass
