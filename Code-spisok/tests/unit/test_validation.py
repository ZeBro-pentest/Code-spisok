import pytest
from src import Code_spisok
    

class TestAdd:
    # ===================== УСПЕШНЫЕ СЛУЧАИ =====================
    @pytest.mark.parametrize(
        "value, expected_list, expected_output",
        [
            ("good", ["good"], "Элемент 'good' добавлен"),
            (123, [123], "Элемент '123' добавлен"),
            (12.32, [12.32], "Элемент '12.32' добавлен"),
        ],
        ids=["str", "int", "float"]
    )
    def test_add_success(self, capsys, value, expected_list, expected_output):
        """Проверяет успешное добавление элемента в список"""
        Code_spisok.my_list.clear()

        result = Code_spisok.add(value)

        # Проверяем содержимое списка
        assert Code_spisok.my_list == expected_list
        assert result == expected_list

        # Проверяем, что print вывел нужный текст
        captured = capsys.readouterr().out
        assert expected_output in captured
        assert Code_spisok.list_name in captured


    # ===================== ОШИБОЧНЫЕ СЛУЧАИ =====================
    @pytest.mark.parametrize(
        "value, exception_type, message",
        [
            (None, ValueError, "Невозможно преобразовать значение"),
            ({}, ValueError, "Невозможно преобразовать значение"),
            ([], ValueError, "Невозможно преобразовать значение"),
            ("error", TypeError, "Ошибка конвертации"),
        ],
        ids=["none", "dict", "list", "str_error"]
    )
    def test_add_exceptions(self, monkeypatch, value, exception_type, message):
        """Проверяет, что add() корректно обрабатывает исключения"""

        Code_spisok.my_list.clear()

        # Переопределим Convert_input так, чтобы он вызывал ошибку
        def mock_convert(x):
            # Имитация разных ошибок в зависимости от входных данных
            if x == "error":
                raise TypeError("Ошибка конвертации")
            else:
                raise ValueError("Невозможно преобразовать значение")

        monkeypatch.setattr(Code_spisok, "Convert_input", mock_convert)

        # Проверяем, что вызывается нужное исключение
        with pytest.raises(exception_type, match=message):
            Code_spisok.add(value)

        # Проверяем, что список остался пустым
        assert Code_spisok.my_list == []
