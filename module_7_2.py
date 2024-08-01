def custom_write(file_name, strings):
    number_of_strings = {}
    with open(file_name, 'w', encoding='utf-8') as f:
        for index, strings in enumerate(strings):
            byte_position = f.tell()
            f.write(strings + '\n')
            number_of_strings[(index + 1, byte_position)] = strings
    return number_of_strings


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
