#Имеется файл JSON с информацией о продуктах: Напишите программу, которая считывает информацию из этого файла и выводит ее на экран в виде:
import json
from pprint import pprint

with open('prod.json', encoding='utf-8') as json_file:
		products_data = json.load(json_file)
		pprint(products_data, indent=3, sort_dicts=False)
		for product in products_data['products']:
			print(f'Название: {product["name"]}\n'
					f'Цена: {product["price"]}\n'
					f'Вес: {product["weight"]}\n'
					f'{"В наличии" if product["available"] else "Нет в наличии!"}\n')