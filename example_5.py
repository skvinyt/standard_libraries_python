import os
import argparse
import logging
from collections import namedtuple

# Определяем namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def gather_directory_info(directory_path):
    # Проверяем, является ли указанный путь директорией
    if not os.path.isdir(directory_path):
        raise ValueError(f"The path {directory_path} is not a directory.")

    # Получаем содержимое директории
    items = os.listdir(directory_path)

    # Собираем информацию о каждом элементе
    info_list = []
    for item in items:
        item_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(item_path)
        if is_directory:
            name = item
            extension = ''
        else:
            name, extension = os.path.splitext(item)
            extension = extension.lstrip('.')  # Удаляем начальную точку из расширения

        parent_directory = os.path.basename(directory_path)
        file_info = FileInfo(name, extension, is_directory, parent_directory)
        info_list.append(file_info)

        # Логируем информацию
        logging.info(file_info)

    return info_list

def main():
    # Настраиваем логирование
    logging.basicConfig(filename='directory_info.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s')

    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Скрипт для сбора информации о содержимом директории.')
    parser.add_argument('directory', type=str, help='Путь к директории')

    # Парсим аргументы командной строки
    args = parser.parse_args()

    # Собираем информацию о содержимом директории
    try:
        directory_info = gather_directory_info(args.directory)
        print("Информация успешно собрана и залогирована.")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
