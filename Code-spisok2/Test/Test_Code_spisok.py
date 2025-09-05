import pytest
import subprocess
# запустить тест " pytest -v .\Test\Test_Code_spisok.py " при это выключить 12 - строчку кода!"

def run_test(user_input: str, expected_outputs: list[str]):
    process = subprocess.run(
        ["python", "Code_spisok.py"], # файл который тестируем!!!
        cwd="Code-spisok2",
        input=user_input,
        capture_output=True,
        text=True,
        encoding="utf-8", # !!!!вот эта штука мешает pytest в консоли!!!!
        timeout=5,
    )
    print("\n=== НАЧАЛО ПРОГРАММЫ ===\n")
    print(process.stdout.strip())  # вывод без лишних пустых строк
    print("\n=== КОНЕЦ ВЫВОДА ===")

# Разбиваем вывод на строки и убираем пустые
    output_lines = [line.strip() for line in process.stdout.splitlines() if line.strip()]
    expected_lines = [line.strip() for line in expected_outputs]

    # Сравниваем построчно
    assert output_lines == expected_lines, (
        f"\nОжидалось:\n{expected_lines}\n\n"
        f"Получено:\n{output_lines}"
    )

    assert process.returncode == 0

# -----------------ТЕСТ-КЕЙСЫ-----------------

class TestHelp: #✅
    @pytest.mark.parametrize("value, expected", [
        ("help", [
            "'Spisok'>>",
            "-----------------------------------------------------------",
            "Список доступных команд:",
            "add       - добавить элемент",
            "clear     - очистить список",
            "el_check  - проверить наличие элемента",
            "exit      - выйти из программы",
            "fd_el     - найти элемент по индексу",
            "fd_ind    - найти индекс элемента по названию",
            "rem_el    - удалить элемент по названию",
            "rem_ind   - удалить элемент по индексу",
            "ren       - переименовать список",
            "rep_el    - заменить элемент по названию",
            "rep_ind   - заменить элемент по индексу",
            "rev       - перевернуть список",
            "show      - показать список",
            "-----------------------------------------------------------"
        ]),
    ])
    def test_help(self, value, expected):
        user_input = f"Spisok\n{value}\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            *expected,  # распаковываем список expected
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])

class TestAdd: #✅
    @pytest.mark.parametrize("value, expected", [
        ("good", "'good'"),    # test 1
        (123, "123"),          # test 2
        (12.32, "12.32"),      # test 3
    ])
    def test_add(self, value, expected):
        user_input = f"Spisok\nadd\n{value}\nshow\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{value}' добавлен в список 'Spisok'.",
            f"'Spisok'>> Содержимое списка 'Spisok':[{expected}]",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])

class TestClear: #✅
    @pytest.mark.parametrize("value, expected", [
        ("mtr", "'mtr'"),      # test 1
        (1456, "1456"),        # test 2
        (13, "13"),            # test 3
    ])
    def test_clear(self, value, expected):
        user_input = f"Spisok\nadd\n{value}\nshow\nclear\nshow\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{value}' добавлен в список 'Spisok'.",
            f"'Spisok'>> Содержимое списка 'Spisok':[{expected}]",
            "'Spisok'>> Список очищен.",
            "'Spisok'>> Содержимое списка 'Spisok':[]",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])

class TestElementCheck: #✅
    @pytest.mark.parametrize("value, expected, type_repr", [
        ("glass", "'glass'", "<class 'str'>"),       # test 1
        (1456, "1456", "<class 'int'>"),             # test 2
        (13.23, "13.23", "<class 'float'>"),         # test 3
    ])
    def test_element_check(self, value, expected, type_repr):
        user_input = f"Spisok\nadd\n{value}\nshow\nel_check\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{value}' добавлен в список 'Spisok'.",
            f"'Spisok'>> Содержимое списка 'Spisok':[{expected}]",
            f"'Spisok'>> [{value}] -- {type_repr} <index '0'>",  # используем полное представление типа
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])

class TestExit: #✅
    @pytest.mark.parametrize("value", [
        ("exit"),       # test 1
    ])
    def test_exit(self, value):
        user_input = f"Spisok\n{value}\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])

class TestFdElement: #✅
    @pytest.mark.parametrize("value, expected", [
        ("Sokelzi", "Sokelzi"),         # test 1
        (14432, "14432"),               # test 2
        (13.234, "13.234"),             # test 3
    ])
    def test_fd_element(self, value, expected):
        user_input = f"Spisok\nadd\n{value}\nfd_el\n0\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{value}' добавлен в список 'Spisok'.",
            f"'Spisok'>> Введите индекс чтобы узнать элемент: Элемент: '{expected}'",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])
    


class TestFdIndex:
    pass

class TestRemove:
    pass

class TestReverse:
    pass

