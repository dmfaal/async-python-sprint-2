import asyncio
from typing import List
from job import Job

class Scheduler:
    def __init__(self, pool_size: int = 10):
        self.pool_size = pool_size
        self.tasks: List[Job] = []
        self._is_running = False

    def schedule(self, task: Job):
        """Добавление задачи в планировщик."""
        self.tasks.append(task)
        print(f"Задача {task.task.__name__} добавлена в планировщик.")

    async def run(self):
        """Запуск планировщика и выполнение задач."""
        self._is_running = True
        while self._is_running and self.tasks:
            # Выбираем задачи для выполнения (ограничение по pool_size)
            current_tasks = self.tasks[: self.pool_size]
            await asyncio.gather(*(task.run() for task in current_tasks))

            # Удаляем выполненные задачи
            self.tasks = self.tasks[self.pool_size :]

        self._is_running = False
        print("Все задачи выполнены.")

    def restart(self):
        """Перезапуск планировщика."""
        self._is_running = True
        print("Планировщик перезапущен.")

    def stop(self):
        """Остановка планировщика."""
        self._is_running = False
        print("Планировщик остановлен.")