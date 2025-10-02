list_name = input("Введите название списка: ")
my_list = []  # создаём пустой список

print(f"Список '{list_name}' создан. Введите команды для управления списком. Список команд - 'help'")

def Convert_input(value): #Функция для определения типа данных
    try:
         # Сначала попробуем преобразовать значение в целое число
        return int(value)
    except ValueError:
        try:
            # Если не целое, попробуем преобразовать в число с плавающей точкой
            return float(value)
        except ValueError:
            # Если не число, возвращаем как строку
            return value

def add():
    element = Convert_input(input("Введите элемент для добавления в список: "))
    my_list.append(element)
    print(f"Элемент '{element}' добавлен в список '{list_name}'.")
    
def ren():
    global list_name
    list_name = input("Введите новое название списка: ")
    print("Список переименован.")
    
def rev():
    my_list.reverse()
    print(f"Перевернутый лист: {my_list}")
    
def show():
    print(f"Содержимое списка '{list_name}':{my_list}")
    
def clear():
    my_list.clear()
    print("Список очищен.")

def el_check():
    if my_list:
        for i in my_list:
            print(f"[{i}] -- {type(i)} <index '{my_list.index(i)}'>")
    else:
        print("Список пуст.")
        
def rem_el():
    element = Convert_input(input("Введите элемент для удаления: "))
    if element in my_list:
        my_list.remove(element)
        print(f"Элемент '{element}' удалён из списка '{list_name}'.")
    else:
        print(f"Элемент '{element}' не найден в списке.")
        
def rem_ind():
    ind:int = Convert_input(input("Введите индекс элемента: "))
    if isinstance(ind, int): 
        try:
            del my_list[ind]
            print(f"Элемент индекса [{ind}] удален из списка '{list_name}'")
        except IndexError:
            print(f"Индекс: '{ind}' вне диапазона!")
    else:
        print("Ошибка: нужно ввести целое число!")
        
def rep_el():
    element1 = Convert_input(input("Введите 'элемент' чтобы заменить его: "))
    if element1 in my_list:
        element2 = Convert_input(input("Введите свой 'элемент', который хотите поставить: "))
        my_list[my_list.index(element1)] = element2
        print(f"Элемент '{element1}' заменён на '{element2}' из списка '{list_name}'")
    else:
        print(f"Элемент '{element1}' не найден в списке.")
        
def rep_ind():
    ind:int = Convert_input(input("Введите 'индекс' чтобы заменить элемент: "))
    if isinstance(ind, int): 
        try:
            element = Convert_input(input("Введите свой 'элемент' который хотите заменить: "))
            my_list[ind] = element
            print(f"Элемент индекса '{ind}' заменён на '{element}' из списка '{list_name}'")
        except IndexError:
            print(f"Индекс: '{ind}' вне диапазона!")
    else:
        print("Ошибка: нужно ввести целое число!")
        
def fd_el():
    ind:int = Convert_input(input("Введите индекс чтобы узнать элемент: "))
    if isinstance(ind, int): 
        try:
            print(f"Элемент: '{my_list[ind]}'")
        except IndexError:
            print(f"Индекс: '{ind}' вне диапазона!")
    else:
        print("Ошибка: нужно ввести целое число!")
        
def fd_ind():
    element:str = Convert_input(input("Введите элемент чтобы узнать индекс: "))
    if element in my_list:
        print(f"Индекс: '{my_list.index(element)}'")
    else:
        print(f"Элемент '{element}' не найден в списке.")
        
def help():
        command_info = """
-----------------------------------------------------------
Список доступных команд:
    add       - добавить элемент
    clear     - очистить список
    el_check  - проверить наличие элемента
    exit      - выйти из программы
    fd_el     - найти элемент по индексу
    fd_ind    - найти индекс элемента по названию
    rem_el    - удалить элемент по названию
    rem_ind   - удалить элемент по индексу
    ren       - переименовать список
    rep_el    - заменить элемент по названию
    rep_ind   - заменить элемент по индексу
    rev       - перевернуть список
    show      - показать список
-----------------------------------------------------------
"""
        print(command_info)


while True:
    command = input(f"'{list_name}'>> ")

    if command == "add":
        add()

    elif command == "ren":
        ren()

    elif command == "rev":
        rev()

    elif command == "show":
        show()
    
    elif command == "clear":
        clear()

    elif command == "exit": # системная функция
        exit = input("Вы точно хотите выйти из программы? [Y]-да [N]-нет : ")
        if exit == "y" or exit == "Y":
            break
        elif exit == "n" or exit == "N":
            pass
        else:
            print("Неизвестная команда. Попробуйте снова.")

    elif command == "el_check":
        el_check()

    elif command == "rem_el":
        rem_el()

    elif command == "rem_ind":
        rem_ind()

    elif command == "rep_el":
        rep_el()

    elif command == "rep_ind":
        rep_ind()

    elif command == "fd_el": # узнать элемент(по индексу)
        fd_el()

    elif command == "fd_ind": # узнать индекс(по элементу)
        fd_ind()

    elif command == "help":
        help()

    else:
        print("Неизвестная команда. Попробуйте снова.")
