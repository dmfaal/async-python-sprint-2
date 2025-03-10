import asyncio
from API_files.utils import CITIES
from tasks import create_directory_and_file, fetch_weather_data, write_json_to_file
from logs_setup import logger
from job import Job
from scheduler import Scheduler


# Асинхронная задача для обработки данных города
async def process_city(city: str, url: str):
    filename = f"{city.lower()}_weather.json"  # Формируем имя файла
    directory = "weather_data"

    # Создаем директорию и файл
    file_path = create_directory_and_file(directory, filename)
    logger.info(f"Файл создан: {file_path}")

    # Получаем данные по ссылке
    data = fetch_weather_data(url)
    if data:
        # Записываем данные в файл
        write_json_to_file(file_path, data)
        logger.info(f"Данные для города {city} успешно записаны в файл: {file_path}")
    else:
        logger.warning(f"Не удалось получить данные для города {city}.")


# Основная функция
async def main():
    # Создаем планировщик
    scheduler = Scheduler(pool_size=5)  # Ограничиваем количество одновременно выполняемых задач

    # Перебираем все города и ссылки из словаря CITIES
    for city, url in CITIES.items():
        # Создаем задачу для каждого города
        task = Job(
            task=lambda city=city, url=url: process_city(city, url),  # Асинхронная задача
            max_working_time=10,  # Максимальное время выполнения задачи (10 секунд)
            tries=2,  # Количество попыток выполнения задачи
        )
        # Явно задаем имя задачи
        task.task.__name__ = f"process_city_{city.lower()}"
        # Добавляем задачу в планировщик
        scheduler.schedule(task)

    # Запускаем планировщик
    await scheduler.run()


# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
