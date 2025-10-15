class ListManager:
    def __init__(self):
        self.list_name = input("Введите название списка: ")
        self.my_list = []
        print(f"Список '{self.list_name}' создан. Введите команды для управления списком. Список команд - 'help'")

        self.commands = {
            "add": self.add,
            "ren": self.ren,
            "rev": self.rev,
            "show": self.show,
            "clear": self.clear,
            "el_check": self.el_check,
            "rem_el": self.rem_el,
            "rem_ind": self.rem_ind,
            "rep_el": self.rep_el,
            "rep_ind": self.rep_ind,
            "fd_el": self.fd_el,
            "fd_ind": self.fd_ind,
            "help": self.help,
            "exit": self.exit_program
        }

    def Convert_input(self, value): #Функция для определения типа данных
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

    def add(self):
        element = self.Convert_input(input("Введите элемент для добавления в список: "))
        self.my_list.append(element)
        print(f"Элемент '{element}' добавлен в список '{self.list_name}'.")

    def ren(self):
        self.list_name = input("Введите новое название списка: ")
        print("Список переименован.")

    def rev(self):
        self.my_list.reverse()
        print(f"Перевернутый лист: {self.my_list}")

    def show(self):
        print(f"Содержимое списка '{self.list_name}':{self.my_list}")

    def clear(self):
        self.my_list.clear()
        print("Список очищен.")

    def el_check(self):
        if self.my_list:
            for i in self.my_list:
                print(f"[{i}] -- {type(i)} <index '{self.my_list.index(i)}'>")
        else:
            print("Список пуст.")

    def rem_el(self):
        element = self.Convert_input(input("Введите элемент для удаления: "))
        if element in self.my_list:
            self.my_list.remove(element)
            print(f"Элемент '{element}' удалён из списка '{self.list_name}'.")
        else:
            print(f"Элемент '{element}' не найден в списке.")

    def rem_ind(self):
        ind = self.Convert_input(input("Введите индекс элемента: "))
        if isinstance(ind, int):
            try:
                del self.my_list[ind]
                print(f"Элемент индекса [{ind}] удален из списка '{self.list_name}'")
            except IndexError:
                print(f"Индекс: '{ind}' вне диапазона!")
        else:
            print("Ошибка: нужно ввести целое число!")

    def rep_el(self):
        element1 = self.Convert_input(input("Введите 'элемент' чтобы заменить его: "))
        if element1 in self.my_list:
            element2 = self.Convert_input(input("Введите свой 'элемент', который хотите поставить: "))
            self.my_list[self.my_list.index(element1)] = element2
            print(f"Элемент '{element1}' заменён на '{element2}' из списка '{self.list_name}'")
        else:
            print(f"Элемент '{element1}' не найден в списке.")

    def rep_ind(self):
        ind = self.Convert_input(input("Введите 'индекс' чтобы заменить элемент: "))
        if isinstance(ind, int):
            try:
                element = self.Convert_input(input("Введите свой 'элемент' который хотите заменить: "))
                self.my_list[ind] = element
                print(f"Элемент индекса '{ind}' заменён на '{element}' из списка '{self.list_name}'")
            except IndexError:
                print(f"Индекс: '{ind}' вне диапазона!")
        else:
            print("Ошибка: нужно ввести целое число!")

    def fd_el(self):
        ind = self.Convert_input(input("Введите индекс чтобы узнать элемент: "))
        if isinstance(ind, int):
            try:
                print(f"Элемент: '{self.my_list[ind]}'")
            except IndexError:
                print(f"Индекс: '{ind}' вне диапазона!")
        else:
            print("Ошибка: нужно ввести целое число!")

    def fd_ind(self):
        element = self.Convert_input(input("Введите элемент чтобы узнать индекс: "))
        if element in self.my_list:
            print(f"Индекс: '{self.my_list.index(element)}'")
        else:
            print(f"Элемент '{element}' не найден в списке.")

    def help(self):
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

    def exit_program(self):
        exit_confirm = input("Вы точно хотите выйти из программы? [Y]-да [N]-нет : ")
        if exit_confirm.lower() == "y":
            return True
        elif exit_confirm.lower() == "n":
            return False
        else:
            print("Неизвестная команда. Попробуйте снова.")
            return False

    def run(self):
        while True:
            command = input(f"'{self.list_name}'>> ").strip()
            func = self.commands.get(command)
            if func:
                if func == self.exit_program:
                    if func():
                        break
                else:
                    func()
            else:
                print("Неизвестная команда. Попробуйте снова.")


if __name__ == "__main__":
    manager = ListManager()
    manager.run()