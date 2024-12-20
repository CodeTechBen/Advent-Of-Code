import pytest

from main import find_xmas

@pytest.mark.parametrize(
    "input, count",
    [
        ("""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""", 18)
    ]
)
def test_find_xmas_expected(input, count):
    assert find_xmas(input) == count