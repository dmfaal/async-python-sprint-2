import os
import json
from API_files.API_client import YandexWeatherAPI
from API_files.utils import CITIES

import os
import json


def create_directory_and_file(directory: str, filename: str) -> str:
    """
    Создает директорию и файл, если они не существуют.
    :param directory: Путь к директории
    :param filename: Имя файла
    :return: Полный путь к созданному файлу
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, filename)
    if not os.path.exists(file_path):
        open(file_path, 'w').close()  # Создаем пустой файл

    return file_path


def fetch_weather_data(url: str):
    """
    Вызывает метод get_forecasting из YandexWeatherAPI.
    :param url: Ссылка на данные о погоде
    :return: Данные в формате JSON или None
    """
    return YandexWeatherAPI.get_forecasting(url)


def write_json_to_file(file_path: str, data: dict):
    """
    Записывает JSON-данные в файл.
    :param file_path: Путь к файлу
    :param data: Данные для записи
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)