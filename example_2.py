from datetime import datetime

# Получаем текущее время и дату
current_datetime = datetime.now()

# Форматируем дату и время в строку с нужным форматом
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Получаем полное название дня недели
day_of_week = current_datetime.strftime('%A')

# Получаем номер недели в году
week_number = current_datetime.isocalendar()[1]

# Выводим результаты
print(f"Текущее время и дата: {formatted_datetime}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")
