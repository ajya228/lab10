#Модифицируйте программу 10.1 – добавьте в нее код, который добавляет данные в файл JSON (спрашивает их у пользователя) и потом также выводить содержимое
# итогового файла на экран.
import json

with open('prod.json', 'r', encoding='utf-8') as json_file:
    products_data: dict = json.load(json_file)
    print('Какой продукт добавить в список? \n')
    products_data['products'].append({
        'name': input('Введите название продукта: '),
        'price': int(input('Введите цену: ')),
        'weight': int(input('Введите вес: ')),
        'available': True if input('Товар доступен? (Да/Нет): ').lower() == 'да' else False})

with open('prod.json', 'w', encoding='utf') as json_file:
    json.dump(products_data, json_file, ensure_ascii=False, indent=4)
