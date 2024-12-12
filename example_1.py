import logging

# Создаем логгер
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Устанавливаем минимальный уровень логирования

# Создаем обработчик для записи логов уровня DEBUG и INFO в файл debug_info.log
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)

# Создаем обработчик для записи логов уровня WARNING и выше в файл warnings_errors.log
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)

# Создаем форматтер для настройки формата сообщений
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Применяем форматтер к обработчикам
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Пример использования логгера
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
