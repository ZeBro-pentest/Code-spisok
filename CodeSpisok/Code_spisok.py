list_name = input("Введите название списка: ")
my_list = []  # создаём пустой список

print(f"Список '{list_name}' создан. Введите команды для управления списком. Список команд - 'help'")

def convert_input(value): #Функция для определения типа данных (число или текст)
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


while True:
    command = input(f"'{list_name}'>> ")

    if command == "add":
        element = convert_input(input("Введите элемент для добавления в список: "))
        my_list.append(element)
        print(f"Элемент '{element}' добавлен в список '{list_name}'.")

    elif command == "ren":
        list_name = input("Введите новое название списка: ")
        print("Список переименован.")

    elif command == "rev":
        my_list.reverse()
        print(f"Перевернутый лист: {my_list}")

    elif command == "show":
        print(f"Содержимое списка '{list_name}':{my_list}")
    
    elif command == "clear":
        my_list.clear()
        print("Список очищен.")

    elif command == "exit":
        exit = input("Вы точно хотите выйти из программы? [Y]-да [N]-нет : ")
        if exit == "y" or exit == "Y":
            break
        elif exit == "n" or exit == "N":
            pass
        else:
            print("Неизвестная команда. Попробуйте снова.")

    elif command == "el_check":
        if my_list:
            for i in my_list:
                print(f"[{i}] -- {type(i)} <index '{my_list.index(i)}'>")
        else:
            print("Список пуст.")

    elif command == "rem_el":
        element = convert_input(input("Введите элемент для удаления: "))
        if element in my_list:
            my_list.remove(element)
            print(f"Элемент '{element}' удалён из списка '{list_name}'.")
        else:
            print(f"Элемент '{element}' не найден в списке.")

    elif command == "rem_ind":
        ind:int = convert_input(input("Введите индекс элемента: "))
        if isinstance(ind, int): 
            try:
                del my_list[ind]
                print(f"Элемент индекса [{ind}] удален из списка '{list_name}'")
            except IndexError:
                print(f"Индекс: '{ind}' вне диапазона!")
        else:
            print("Ошибка: нужно ввести целое число!")

    elif command == "rep_el":
        element1 = convert_input(input("Введите 'элемент' чтобы заменить его: "))
        if element1 in my_list:
            element2 = convert_input(input("Введите свой 'элемент', который хотите поставить: "))
            my_list[my_list.index(element1)] = element2
            print(f"Элемент '{element1}' заменён на '{element2} из списка '{list_name}''")
        else:
            print(f"Элемент '{element1}' не найден в списке.")

    elif command == "rep_ind":
        ind:int = convert_input(input("Введите 'индекс' чтобы заменить элемент: "))
        if isinstance(ind, int): 
            try:
                element = convert_input(input("Введите свой 'элемент' который хотите заменить: "))
                my_list[ind] = element
                print(f"Элемент индекса '{ind}' заменён на '{element}' из списка '{list_name}'")
            except IndexError:
                print(f"Индекс: '{ind}' вне диапазона!")
        else:
            print("Ошибка: нужно ввести целое число!")

    elif command == "fd_el": # узнать элемент(по индексу)
        ind:int = convert_input(input("Введите индекс чтобы узнать элемент: "))
        if isinstance(ind, int): 
            try:
                print(f"Элемент: '{my_list[ind]}'")
            except IndexError:
                print(f"Индекс: '{ind}' вне диапазона!")
        else:
            print("Ошибка: нужно ввести целое число!")

    elif command == "fd_ind": # узнать индекс(по элементу)
        element:str = convert_input(input("Введите элемент чтобы узнать индекс: "))
        if element in my_list:
            print(f"Индекс: '{my_list.index(element)}'")
        else:
            print(f"Элемент '{element}' не найден в списке.")

    elif command == "help":
        print("-----------------------------------------------------------")
        print("Список доступных команд:")
        print()
        print("1     add       - добавить элемент")
        print("2     clear     - очистить список")
        print("3     el_check  - проверить наличие элемента")
        print("4     exit      - выйти из программы")
        print("5     fd_el     - найти элемент по индексу")
        print("6     fd_ind    - найти индекс элемента по названию")
        print("7     rem_el    - удалить элемент по названию")
        print("8     rem_ind   - удалить элемент по индексу")
        print("9     ren       - переименовать список")
        print("10    rep_el    - заменить элемент по названию")
        print("11    rep_ind   - заменить элемент по индексу")
        print("12    rev       - перевернуть список")
        print("13    show      - показать список")
        print("-----------------------------------------------------------")

    else:
        print("Неизвестная команда. Попробуйте снова.")