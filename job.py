import asyncio
from typing import List, Callable, Coroutine


class Job:
    def __init__(
            self,
            task: Callable[[], Coroutine],  # Асинхронная задача
            start_at: str = "",  # Время начала (пока не используется)
            max_working_time: int = -1,  # Максимальное время выполнения (в секундах)
            tries: int = 0,  # Количество попыток выполнения
            dependencies: List["Job"] = [],  # Зависимости (другие задачи)
    ):
        self.task = task
        self.start_at = start_at
        self.max_working_time = max_working_time
        self.tries = tries
        self.dependencies = dependencies
        self._is_running = False
        self._is_paused = False
        self._is_stopped = False

    async def run(self):
        """Запуск задачи."""
        if self._is_stopped:
            print("Задача остановлена и не может быть запущена.")
            return

        # Проверяем зависимости
        for dependency in self.dependencies:
            if not dependency._is_running:
                print(f"Ожидание выполнения зависимости: {dependency.task.__name__}")
                await dependency.run()

        self._is_running = True
        self._is_paused = False

        try:
            # Выполняем задачу с учетом ограничений
            if self.max_working_time > 0:
                await asyncio.wait_for(self.task(), timeout=self.max_working_time)
            else:
                await self.task()
        except asyncio.TimeoutError:
            print(f"Задача {self.task.__name__} превысила максимальное время выполнения.")
        except Exception as e:
            print(f"Ошибка в задаче {self.task.__name__}: {e}")
            if self.tries > 0:
                self.tries -= 1
                print(f"Повторная попытка выполнения задачи {self.task.__name__}...")
                await self.run()
        finally:
            self._is_running = False

    def pause(self):
        """Приостановка задачи."""
        if self._is_running:
            self._is_paused = True
            print(f"Задача {self.task.__name__} приостановлена.")

    def stop(self):
        """Остановка задачи."""
        self._is_stopped = True
        print(f"Задача {self.task.__name__} остановлена.")
