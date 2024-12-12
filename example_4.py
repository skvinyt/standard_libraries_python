import argparse

def main():
    # Создаем объект парсера
    parser = argparse.ArgumentParser(description='Скрипт для обработки числа и строки.')

    # Добавляем обязательные аргументы
    parser.add_argument('number', type=int, help='Число')
    parser.add_argument('text', type=str, help='Строка')

    # Добавляем опцию --verbose
    parser.add_argument('--verbose', action='store_true', help='Включить дополнительный вывод')

    # Добавляем опцию --repeat
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')

    # Парсим аргументы командной строки
    args = parser.parse_args()

    # Если установлен флаг --verbose, выводим дополнительную информацию
    if args.verbose:
        print(f"Получено число: {args.number}")
        print(f"Получена строка: {args.text}")
        print(f"Количество повторений: {args.repeat}")

    # Повторяем строку указанное количество раз
    repeated_text = args.text * args.repeat

    # Выводим результат
    print(repeated_text)

if __name__ == '__main__':
    main()
