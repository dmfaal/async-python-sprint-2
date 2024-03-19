import logging
import pickle


class Scheduler:
    def __init__(self, pool_size: int = 10) -> None:
        logging.info("Инициализация пула задач")
        self.pool_size = pool_size
        self.running_tasks = []
        self.pending_tasks = []

    def schedule(self, task) -> None:
        logging.info("Старт задачника")
        if len(self.running_tasks) < self.pool_size:
            self.running_tasks.append(task)
            task.execute()
        else:
            self.pending_tasks.append(task)

    def run(self) -> None:
        for task in self.running_tasks:
            task.execute()

    def restart(self):
        state = {
            'running_tasks': self.running_tasks,
            'pending_tasks': self.pending_tasks
        }
        with open('scheduler_state.pkl', 'wb') as file:
            pickle.dump(state, file)

    def stop(self):
        pass
