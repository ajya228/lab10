#Требуется создать русско-английский словарь и вывести его в файл ru-en.txt в представленном формате:

en_ru_dict = {}
with open('en-ru.txt', encoding='utf-8') as text_file:
	text_list = [translation.rstrip('\n') for translation in text_file]
	for line in text_list:
		key, value = line.split(' - ')
		en_ru_dict[key] = tuple(value.split(', '))
with open('ru-en.txt', 'w', encoding='utf-8') as text_file:
	ru_en_dict: dict = {value: key for key, value in en_ru_dict.items()}
	ru_en_dict = dict(sorted(ru_en_dict.items(), key=lambda item: item[0]))
	for key, value in ru_en_dict.items():
		print(f'{", ".join(key)} - {value}', file=text_file)