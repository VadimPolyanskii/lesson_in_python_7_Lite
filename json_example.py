
# Создадим файл json

# Пдключаем модель json
import json

dict_avto = {'brand': 'Volvo', 'Model': 'S60', 'Year': '2021', 'Price (million) ': '3.0'}

# Создадим файл json
with open('data_avto.json', 'w') as f:
    json.dump(dict_avto, f)