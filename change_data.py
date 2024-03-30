from return_data_file import data_file

def change_row():
    data, nf = data_file()
    count = len(data)
    num_row = int(input("Введите номер строки: "))
    #del data[num_row -1]

    name = (input("Введите имя: "))
    surname = (input("Введите фамилию: "))
    birth = (input("Введите дату рождения: "))
    city = (input("Введите город: "))

    new_data_row = str(num_row) + ";" + name + ";" + surname + ";" + birth + ";" + city + '\n'

    data[num_row - 1] = new_data_row

    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)

#delete_row()