import pytest
import subprocess

def run_test(user_input: str, expected_outputs: list[str]):
    process = subprocess.run(
        ["python", "Code_Spisok.py"],
        input=user_input,
        capture_output=True,
        text=True,
        timeout=5
    )
    print("\n=== НАЧАЛО ПРОГРАММЫ ===\n")
    print(process.stdout.strip())  # вывод без лишних пустых строк
    print("\n=== КОНЕЦ ВЫВОДА ===")

    for expected in expected_outputs:
        assert expected in process.stdout
    assert process.returncode == 0

class TestHelp:
    pass

class TestAdd:
    @pytest.mark.parametrize("value, expected", [
        ("LOX", "'LOX'"),
        ("123", "123"),
        ("12.32", "12.32"),
    ])
    def test_add_various(self, value, expected):
        user_input = (
            "Spisok\nadd\n" + str(value) + "\nshow\nexit\ny\n"
        )
        run_test(user_input, [
            "Список 'Spisok' создан",
            f"Элемент '{value}' добавлен в список 'Spisok'",
            f"Содержимое списка 'Spisok':[{'{}'.format(expected)}]",
            "Вы точно хотите выйти из программы?"
        ])

class TestClear:
    def test_clear_list(self):
        user_input = (
            "Spisok\nadd\nX\nclear\nshow\nexit\ny\n"
        )
        run_test(user_input, [
            "Список 'Spisok' создан",
            "Элемент 'X' добавлен в список 'Spisok'",
            "Список очищен.",
            "Содержимое списка 'Spisok':[]"
        ])

class TestElementCheck:
    pass

class TestRemove:
    def test_remove_element(self):
        user_input = (
            "Spisok\nadd\n1\nrem_el\n1\nshow\nexit\ny\n"
        )
        run_test(user_input, [
            "Элемент '1' добавлен в список 'Spisok'",
            "Элемент '1' удалён из списка 'Spisok'",
            "Содержимое списка 'Spisok':[]"
        ])

class TestReverse:
    def test_reverse_list(self):
        user_input = (
            "Spisok\nadd\n1\nadd\n2\nrev\nshow\nexit\ny\n"
        )
        run_test(user_input, [
            "Перевернутый лист: [2, 1]",
            "Содержимое списка 'Spisok':[2, 1]"
        ])
