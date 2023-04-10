"""задача38:
Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
функционал для изменения и удаления данных

Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны 
находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)"""

def show_menu():
    print("\nВыберите необходимое действие:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Изменить информацию об абоненте\n"
    "6. Удалить информацию об абоненте\n"
    "7. Сохранение в текстовом формате\n"
    "8. Закончить работу")
    

import csv

def show_all_phonebook(phbook):
        for lines in phbook:
            print(*lines)

def find_lastname(phbook):
    last_name = input("Введите фамилию:  ")
    for elem in filter(lambda x: last_name in x[0].lower(), phbook):
        print(f"Фамилия: {elem[0]}\nимя: {elem[1]}\nтелефон: {elem[2]}\nкомментарий: {elem[3]}\n")

def find_phone_number(phbook):
    phone_number = input("Введите номер телефона:  ")
    for elem in filter(lambda x: phone_number in x[2], phbook):
        print(f"Фамилия: {elem[0]}\nимя: {elem[1]}\nтелефон: {elem[2]}\nкомментарий: {elem[3]}\n")

def add_line_to_phonebook():
    with open("phonebook.csv", "a", encoding="utf-8", newline="") as out_file:
        phbook = csv.reader(out_file)
        new_line = input("Введите данные через пробел: ").split()
        csv.writer(out_file).writerow(new_line)
        print("Информация добавлена")

def change_info():
            for elem in enumerate(list(phbook)):
                print(*elem)
            changed_line = int(input("Какую строку изменяем? "))
            for i in range(len(phbook)):
                if i == changed_line:
                    phbook[i][0] = input("Новая фамилия:")
                    phbook[i][1] = input("Имя:")
                    phbook[i][2] = input("телефон:")
                    phbook[i][3] = input("комментарий:")
            with open("phonebook.csv", "w", encoding="utf-8", newline="") as out_file:
                writer = csv.writer(out_file)
                writer.writerows(phbook)
            print("Информация изменена")
                

def delete_info():
        for elem in enumerate(list(phbook)):
            print(*elem)
        index_del = int(input("Какую строку удаляем? "))
        del phbook[index_del] 
        with open("phonebook.csv", "w", encoding="utf-8", newline="") as out_file:
            writer = csv.writer(out_file)
            writer.writerows(phbook)
        print("Информация удалена")
            
def txt_saving():
    with open("phonebook.csv", "r", encoding="utf-8") as file:
        phbook = list(csv.reader(file))
    with open("phonebook.txt", "w", encoding="utf-8", newline="") as out_file:
        for elem in phbook:
            print(*elem, sep = " ", end = "\n", file = out_file)
    print("Информация сохранена в phonebook.txt")    

show_menu()
for elem in iter(input, "8"):
    
    with open("phonebook.csv", "r", encoding="utf-8") as file:
        phbook = list(csv.reader(file))
        
        if elem =="1":
            show_all_phonebook(phbook)
        if elem =="2":
            find_lastname(phbook)
        if elem =="3":
           find_phone_number(phbook)
        if elem =="4":
           add_line_to_phonebook() 
        if elem =="5":
            change_info()
        if elem =="6":
            delete_info()
        if elem =="7":
            txt_saving()



   
    
    
    
    



