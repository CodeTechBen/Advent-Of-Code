import pytest
from red_nosed_report import is_safe


@pytest.mark.parametrize(
    "input, expected",
    [
     ("", True)  
    ]
)
def test_safe_line_base_case(input, expected):
    assert safe_line(input) == expected



@pytest.mark.parametrize(
    "input, expected_exception",
    [
        ("", ValueError),
        ([1, 2, 3, 4, 5], TypeError),
    ]
)
def test_safe_line_error_case(input, expected_exception):
    with pytest.raises(expected_exception):
        safe_line(input)
