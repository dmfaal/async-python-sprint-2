import logging


# Настройка уровня и файла логирования
def logs():
    logger_settings = logging.getLogger(__name__)

    logging.basicConfig(filename='logs.txt', level=logging.INFO,
                        format='')

    return logger_settings
