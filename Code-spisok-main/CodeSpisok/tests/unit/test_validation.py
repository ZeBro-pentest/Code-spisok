import pytest
from src.Code_spisok import convert_input

@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1", ["1"]),
        ("5 -1 -5", ["5", "-1", "-5"]),
        ("1 2 3 4 5", ["1", "2", "3", "4", "5"]),
    ]
)
def test_convert_input(input_data, expected):
    assert convert_input(input_data) == expected