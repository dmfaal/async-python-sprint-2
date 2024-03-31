import json
import logging
from urllib.request import urlopen
from typing import Generator
import os

from logger.logger import my_logs

logger = my_logs()


def create_rep(dir_name: str) -> Generator:
    """
    Создать папку, если папка создана - удалить папку
    """
    logging.info("Задача: работа с файловой системой")
    try:
        os.mkdir(dir_name)
        logging.info("Папка создана")
        yield
        if os.path.exists(dir_name):
            os.rmdir(dir_name)
            logging.info("Папка удалена")
        yield
    except Exception as ex:
        logging.error(f"Ошибка работы с файловой системой {ex}")
        yield


def request(url: str) -> Generator:
    """
    Запросить данные по ссылке, выполнить декодинг, обработать ответ,
    получить код ответа HTTP и тип ответа (content type)
    """
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
            yield data
    except Exception as ex:
        logging.error(f"Ошибка запроса, получен ответ {ex}")
    yield None


def file(data) -> Generator:
    """
    Создать файл, записать ответ из NetworkTask в файл,
    прочитать файл, удалить файл
    """
    logging.info("Задача: работа с файлами")
    try:
        with open("test_file.txt", "w") as file:
            file.write(str(data))
            logging.info(f"Записано содержимое {data}")
    except Exception as ex:
        logging.error(f"Ошибка работы с файлом {ex}")
    yield
    try:
        with open("test_file.txt", "r") as file:
            written_data = file.read()
            logging.info(f"Содержимое файла: {written_data}")
    except Exception as ex:
        logging.error(f"Ошибка чтения: {ex}")
    try:
        os.remove("C:\\Users\\d.fadeev\\Desktop\\async-python-sprint-2\\test_file.txt")
    except Exception as ex:
        logging.error(f"Ошибка удаления: {ex}")
    yield



