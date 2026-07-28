import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("hello", "Hello"),
    ("cats", "Cats"),
    ("hello world", "Hello world"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("  ", "  "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" hello ", "hello "),
    ("  welcome", "welcome"),
    ("python ", "python "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("car", "car"),
    ("", ""),
    ("  ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, substring, expected", [
    ("hello world", "world", True),
    ("hello world", "hello", True),
    ("Python", "Py", True),
    ("12345", "23", True),
    ("hello world", "python", False)
])
def test_contains_positive(string, substring, expected):
    assert string_utils.contains(string, substring) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, substring, expected", [
    ("", "", True),
    ("", "hello", False),
    (" ", " ", True)
])
def test_contains_negative(string, substring, expected):
    assert string_utils.contains(string, substring) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, index, expected", [
    ("hello", 0, "ello"),
    ("hello", 4, "hell"),
    ("abcde", 1, "acde"),
])
def test_delete_symbol_positive(input_str, index, expected):
    assert string_utils.delete_symbol(input_str, index) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, index, expected", [
    ("hello", 5, "hello"),
    ("", 0, ""),
])
def test_delete_symbol_negative(input_str, index, expected):
    assert string_utils.delete_symbol(input_str, index) == expected
