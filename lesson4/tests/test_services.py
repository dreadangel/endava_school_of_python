from lesson4.app.services.services import capital_case, divide
import pytest


def test_capital_case_ok():
    assert capital_case("igor") == "Igor"


def test_divide_positive_numbers() -> None:
    assert divide(1, 2) == 0.5
    
    
def test_divide_raises_exception_on_zero_arguments():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)