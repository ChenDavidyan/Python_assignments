import file_counter
import pytest


@pytest.mark.parametrize("text, expected", [("blabla", 6), ("Chen", 4), ("", 0)])
def test_char_cnt(text, expected):
    result = file_counter.char_cnt(text)
    assert result == expected


@pytest.mark.parametrize(
    "text, expected",
    [("blabla", 1), ("Chen \n Davidyan", 2), ("sv \n rv \n wr", 3), ("", 0)],
)
def test_add_parametrize(text, expected):
    result = file_counter.lines_cnt(text)
    assert result == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("blabla", 1),
        ("Chen Davidyan", 2),
        ("hello world! My name is Chen", 6),
        ("", 0),
        ("1 2 3 4 5 6 7 8 9", 9),
    ],
)
def test_add_parametrize(text, expected):
    result = file_counter.words_cnt(text)
    assert result == expected
