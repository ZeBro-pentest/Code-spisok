import pytest
import subprocess
import os

def run_test(user_input: str, expected_outputs: list[str]):
    # Правильный путь к файлу
    file_path = os.path.join("src/Code_spisok.py")
    
    process = subprocess.run(
        ["python", file_path],  # правильный путь к файлу
        cwd="CodeSpisok",     # рабочая директория
        input=user_input,
        capture_output=True,
        text=True,
        encoding="utf-8", # мешает запускать в cmd!!!
        timeout=5,
    )
    
    print("\n=== НАЧАЛО ПРОГРАММЫ ===\n")
    print(process.stdout.strip())
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
        ("good", "'good'"),    # test 1  test 1 кавычки необходимы для команды show и rev
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
        ("Sokelzi", "Sokelzi"),         # test 1
        (14432, "14432"),               # test 2
        (13.234, "13.234"),             # test 3
    ])
    def test_clear(self, value, expected):
        user_input = f"Spisok\nadd\n{value}\nclear\nshow\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{expected}' добавлен в список 'Spisok'.",
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
            f"'Spisok'>> [{value}] -- {type_repr} <index '0'>",  # используем полное представление типа, индекс 0 потомучто элемент один
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])

class TestExit: #✅
    @pytest.mark.parametrize("value, expected",[
        ("exit", "Вы точно хотите выйти из программы? [Y]-да [N]-нет : "),       # test 1
    ])
    def test_exit(self, value, expected):
        user_input = f"Spisok\n{value}\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> {expected}"
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
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{expected}' добавлен в список 'Spisok'.",
            # test
            f"'Spisok'>> Введите индекс чтобы узнать элемент: Элемент: '{expected}'",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])
    
class TestFdIndex: #✅
    @pytest.mark.parametrize("value, expected",[
        ("Sokelzi", "Sokelzi"),         # test 1
        (14432, "14432"),               # test 2
        (13.234, "13.234"),             # test 3
    ])
    def test_fd_index(self, value, expected):
        user_input = f"Spisok\nadd\n{value}\nfd_ind\n{value}\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{expected}' добавлен в список 'Spisok'.",
            # test
            f"'Spisok'>> Введите элемент чтобы узнать индекс: Индекс: '0'",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])

class TestRem_el: #✅
    @pytest.mark.parametrize("value, expected",[
        ("Sokelzi", "Sokelzi"),         # test 1
        (14432, "14432"),               # test 2
        (13.234, "13.234"),             # test 3
    ])
    def test_rm_element(self, value, expected):
        user_input = f"Spisok\nadd\n{value}\nrem_el\n{value}\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{expected}' добавлен в список 'Spisok'.",
            # test
            f"'Spisok'>> Введите элемент для удаления: Элемент '{expected}' удалён из списка 'Spisok'.",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])

class TestRem_ind: #✅
    @pytest.mark.parametrize("value, expected",[
        ("Sokelzi", "Sokelzi"),         # test 1
        (14432, "14432"),               # test 2
        (13.234, "13.234"),             # test 3
    ])
    def test_rm_index(self, value, expected):
        user_input = f"Spisok\nadd\n{value}\nrem_ind\n0\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{expected}' добавлен в список 'Spisok'.",
            # test
            f"'Spisok'>> Введите индекс элемента: Элемент индекса [0] удален из списка 'Spisok'",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])
    
class TestRen: #✅
    @pytest.mark.parametrize("value, expected",[
        ("Sokelzi", "Sokelzi"),           # test 1
        (14432, "14432"),                 # test 2
        (13.234, "13.234"),               # test 3
    ])
    def test_ren(self, value, expected):
        user_input = f"Spisok\nren\n{value}\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            # test
            "'Spisok'>> Введите новое название списка: Список переименован.",
            f"'{expected}'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])
    
class TestRep_el: #✅
    @pytest.mark.parametrize("value, expected, value2, expected2",[
        ("Sokelzi", "Sokelzi", "Sokelzi2", "Sokelzi2"),           # test 1
        (14432, "14432", 282828, "282828"),                       # test 2
        (13.234, "13.234", 29.29, "29.29"),                       # test 3
    ])
    def test_rep_element(self, value, expected, value2, expected2):
        user_input = f"Spisok\nadd\n{value}\nrep_el\n{value}\n{value2}\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{expected}' добавлен в список 'Spisok'.",
            # test
            f"'Spisok'>> Введите 'элемент' чтобы заменить его: Введите свой 'элемент', который хотите поставить: Элемент '{expected}' заменён на '{expected2}' из списка 'Spisok'",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])
        
class TestRep_ind: #✅
    @pytest.mark.parametrize("value, expected, value2, expected2",[
        ("Sokelzi", "Sokelzi", "Sokelzi2", "Sokelzi2"),           # test 1
        (14432, "14432", 282828, "282828"),                       # test 2
        (13.234, "13.234", 29.29, "29.29"),                       # test 3
    ])
    def test_rep_index(self, value, value2, expected, expected2):
        user_input = f"Spisok\nadd\n{value}\nrep_ind\n0\n{value2}\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{expected}' добавлен в список 'Spisok'.",
            # test
            f"'Spisok'>> Введите 'индекс' чтобы заменить элемент: Введите свой 'элемент' который хотите заменить: Элемент индекса '0' заменён на '{expected2}' из списка 'Spisok'",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])
        
class TestRev: #✅
        @pytest.mark.parametrize("value, value2, value3, expected1, expected2, expected3",[
        ("Sokelzi", 14432, 13.234, "'Sokelzi'", 14432, 13.234),         # test 1 кавычки необходимы для команды show и rev
    ])
        def test_revers(self, value, value2, value3, expected1, expected2, expected3):
            user_input = f"Spisok\nadd\n{value}\nadd\n{value2}\nadd\n{value3}\nshow\nrev\nexit\ny\n"
            
            run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{value}' добавлен в список 'Spisok'.",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{value2}' добавлен в список 'Spisok'.",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{value3}' добавлен в список 'Spisok'.",
            # test
            f"'Spisok'>> Содержимое списка 'Spisok':[{expected1}, {expected2}, {expected3}]",
            f"'Spisok'>> Перевернутый лист: [{expected3}, {expected2}, {expected1}]",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
            ])
            
class TestShow: #✅
    @pytest.mark.parametrize("value, expected", [
        ("Sokelzi", "'Sokelzi'"),           # test 1 кавычки необходимы для команды show и rev
        (14432, "14432"),                   # test 2
        (13.234, "13.234"),                 # test 3
    ])
    def test_exit(self, value, expected):
        user_input = f"Spisok\nadd\n{value}\nshow\nexit\ny\n"
        
        run_test(user_input, [
            "Введите название списка: Список 'Spisok' создан. Введите команды для управления списком. Список команд - 'help'",
            f"'Spisok'>> Введите элемент для добавления в список: Элемент '{value}' добавлен в список 'Spisok'.",
            # test
            f"'Spisok'>> Содержимое списка 'Spisok':[{expected}]",
            "'Spisok'>> Вы точно хотите выйти из программы? [Y]-да [N]-нет :"
        ])