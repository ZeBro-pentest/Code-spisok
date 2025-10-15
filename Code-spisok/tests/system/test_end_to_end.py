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
        encoding="utf-8",
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

class Test_end_to_end:
    pass