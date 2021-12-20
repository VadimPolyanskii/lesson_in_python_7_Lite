# Создание файла csv

import csv          # Импортируем модуль csv


# Создаем данные для заполнения в csv
car_data = [['brand', 'model', 'year', 'price (mln)'], ['Scoda', 'Octavia', '2021', '1.7'], ['Merсedes-Benz', 'GLA',
            '2021', '3.2'], ['Volvo', 'S60', '2021', '3.0']]


# Создадим csv файл
with open('data_avto.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(car_data)