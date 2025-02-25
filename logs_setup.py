import logging


# Настройка уровня и файла логирования
def setup_logger():
    # Настройка формата логов
    log_format = '%(asctime)s - %(levelname)s - %(message)s'

    # Настройка базовой конфигурации логирования
    logging.basicConfig(
        level=logging.INFO,  # Уровень логирования (INFO и выше)
        format=log_format,  # Формат логов
        handlers=[
            logging.FileHandler('logs.txt', mode='w'),  # Запись в файл
            logging.StreamHandler()  # Вывод в консоль
        ]
    )


# Инициализация логгера
setup_logger()

# Пример использования
logger = logging.getLogger(__name__)
logger.info("Это информационное сообщение.")
logger.warning("Это предупреждение.")
logger.error("Это ошибка.")
