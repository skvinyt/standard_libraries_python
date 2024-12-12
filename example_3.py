from datetime import datetime, timedelta

def get_future_date(days):
    # Получаем текущую дату и время
    current_datetime = datetime.now()

    # Создаем объект timedelta для указанного количества дней
    delta = timedelta(days=days)

    # Добавляем timedelta к текущей дате
    future_datetime = current_datetime + delta

    # Форматируем дату в строку с нужным форматом
    future_date_str = future_datetime.strftime('%Y-%m-%d')

    # Возвращаем и выводим дату
    return future_date_str

# Пример использования функции
days_to_add = 15
future_date = get_future_date(days_to_add)
print(f"Дата через {days_to_add} дней: {future_date}")
