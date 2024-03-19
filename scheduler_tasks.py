import concurrent.futures
import csv
import json
import logging
from http import HTTPStatus
from urllib.request import urlopen
from urllib.error import HTTPError

import os
import time
import requests

from logger.logger import my_logs
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from scheduler_data.URL import url

logger = my_logs()


class FileSystemTask:
    """
    Создать папку, если папка создана - удалить папку
    """

    def __init__(self, dir_name):
        self.dir_name = dir_name

    def create_directory(self):
        logging.info("Задача: работа с файловой системой")
        try:
            os.mkdir(self.dir_name)
            logging.info("Папка создана")
            yield
            if os.path.exists(self.dir_name):
                os.rmdir(self.dir_name)
                logging.info("Папка удалена")
            yield
        except Exception as ex:
            logging.error(f"Ошибка работы с файловой системой {ex}")
            yield


class NetworkTask:
    """
    Запросить данные по ссылке, выполнить декодинг, обработать ответ,
    получить код ответа HTTP и тип ответа (content type)
    """

    @staticmethod
    def request(url: str) -> str:
        try:
            with urlopen(url) as response:
                logging.info("Задача: работа с сетью")
                resp_body = response.read().decode("utf-8")
                data = json.loads(resp_body)

                http_code = response.getcode()
                http_response_type = response.info().get_content_type()

                logging.info(f"Получен ответ: {data}")
                logging.info(f"Код ответа HTTP: {http_code}")
                logging.info(f"Тип ответа HTTP: {http_response_type}")
        except Exception as ex:
            logging.error(f"Ошибка запроса, получен ответ {ex}")
        yield


class FilesTask:
    """
    Создать файл, записать ответ из NetworkTask в файл,
    прочитать файл
    """

    def __init__(self, file_name):
        self.dir_name = file_name

    def file(self, data):
        logging.info("Задача: работа с файлами")
        try:
            with open("test_file.txt", "w") as file:
                file.write(data)
                logging.info(f"Записано содержимое {data}")
        except Exception as ex:
            logging.error(f"Ошибка работы с файлом {ex}")
        yield
        try:
            with open("test_file.txt", "r") as file:
                written_data = file.read()
                logging.info(f"Содержимое файла: {written_data}")
        except Exception as ex:
            logging.error(f"Не удалось прочитать содержимое {ex}")
        yield


def main():
    FileSystemTask("task_directory")
    NetworkTask()
    FilesTask("my_file.txt")


if __name__ == "__main__":
    main()
