from API_files.utils import CITIES
from tasks import create_directory_and_file, fetch_weather_data, write_json_to_file
from logs_setup import logger


def main():
    directory = "weather_data"  # Директория для хранения файлов

    # Перебираем все города и ссылки из словаря CITIES
    for city, url in CITIES.items():
        filename = f"{city.lower()}_weather.json"  # Формируем имя файла
        file_path = create_directory_and_file(directory, filename)  # Создаем файл

        # Получаем данные по ссылке
        data = fetch_weather_data(url)

        if data:
            # Записываем данные в файл
            write_json_to_file(file_path, data)
            logger.info(f"Данные для города {city} успешно записаны в файл: {file_path}")
        else:
            logger.warning(f"Не удалось получить данные для города {city}.")


if __name__ == "__main__":
    main()
