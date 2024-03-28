from return_data_file import data_file


def delete_row():
    data, nf = data_file()
    count = len(data)
    num_row= int(input("Введите номер строки: "))
    del data[num_row-1]
    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)

#delete_row()