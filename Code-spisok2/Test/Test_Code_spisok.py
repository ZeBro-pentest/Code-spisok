import pytest
import subprocess
# запустить тест " pytest -v .\Test\Test_Code_spisok.py ""

def run_test(user_input: str, expected_outputs: list[str]):
    process = subprocess.run(
        ["python", "Code_spisok.py"], # файл который тестируем!!!
        input=user_input,
        capture_output=True,
        text=True,
        encoding="utf-8", # !!!!вот эта штука мешает pytest в консоли!!!!
        timeout=5
    )
    print("\n=== НАЧАЛО ПРОГРАММЫ ===\n")
    print(process.stdout.strip())  # вывод без лишних пустых строк
    print("\n=== КОНЕЦ ВЫВОДА ===")

    for expected in expected_outputs:
        assert expected in process.stdout
    assert process.returncode == 0

# -----------------ТЕСТ-КЕЙСЫ-----------------

class TestHelp:
    pass

class TestAdd: #✅
    @pytest.mark.parametrize("value, expected", [
        ("good", "'good'"),    # test 1
        (123, 123),          # test 2
        (12.32, 12.32),      # test 3
    ])
    def test_add_various(self, value, expected):
        user_input = (
            "Spisok\nadd\n" + str(value) + "\nshow\nexit\ny\n"
        )
        run_test(user_input, [
            "Список 'Spisok' создан",
            f"Элемент '{value}' добавлен в список 'Spisok'",
            f"Содержимое списка 'Spisok':[{expected}]",
            "Вы точно хотите выйти из программы?"
        ])

class TestClear: #✅ (15-16 знаков после запятой — предел точности float)
    @pytest.mark.parametrize("value, expected", [
        ("mtr", "'mtr'"),      # test 1
        (1456, 1456),          # test 2
        (13, 13),              # test 3
    ])
    def test_add_various(self, value, expected):
        user_input = (
            "Spisok\nadd\n" + str(value) + "\nshow\nclear\nshow\nexit\ny\n"
        )
        run_test(user_input, [
            "Список 'Spisok' создан",
            f"Элемент '{value}' добавлен в список 'Spisok'",
            f"Содержимое списка 'Spisok':[{expected}]",
            "Список очищен.",
            f"Содержимое списка 'Spisok':[{expected}]",
            "Вы точно хотите выйти из программы?"
        ])

class TestElementCheck: #✅
    @pytest.mark.parametrize("value, expected", [
        ("glass", "'glass'"),       # test 1
        (1456, 1456),               # test 2
        (13.23, 13.23),             # test 3
    ])
    def test_add_various(self, value, expected):
        user_input = (
            "Spisok\nadd\n" + str(value) + "\nshow\nel_check\nexit\ny\n"
        )
        run_test(user_input, [
            "Список 'Spisok' создан",
            f"Элемент '{value}' добавлен в список 'Spisok'",
            f"Содержимое списка 'Spisok':[{expected}]",
            f"[{value}] -- {type(value)} <index '0'>",      # индекс 0 т.к елемент один
            f"Содержимое списка 'Spisok':[{expected}]",
            "Вы точно хотите выйти из программы?"
        ])

class TestExit: #✅
    @pytest.mark.parametrize("value", [
        ("exit"),       # test 1
    ])
    def test_add_various(self, value):
        user_input = (
            "Spisok\n" + (value) + "\ny\n"
        )
        run_test(user_input, [
            "Список 'Spisok' создан",
            "Вы точно хотите выйти из программы?"
        ])

class TestFdElement: #✅
    @pytest.mark.parametrize("value, expected", [
        ("Sokelzi", "'Sokelzi'"),       # test 1
        (14432, 14432),                 # test 2
        (13.234, 13.234),               # test 3
    ])
    def test_add_various(self, value, expected):
        user_input = (
            "Spisok\nadd\n" + str(value) + "\nfd_el\n0\nexit\ny\n"
        )
        run_test(user_input, [
            "Список 'Spisok' создан",
            f"Элемент '{value}' добавлен в список 'Spisok'",
            f"Элемент: '{value}'",
            "Вы точно хотите выйти из программы?"
        ])
    


class TestFdIndex:
    pass

class TestRemove:
    pass

class TestReverse:

    pass
