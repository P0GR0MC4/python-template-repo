"""Moduł zawierający testy jednostkowe dla funkcji kalkulatora."""

from logic.calculator import add, subtract


def test_add() -> None:
    """Testuje poprawność działania funkcji dodawania."""
    assert add(2.0, 3.0) == 5.0
    assert add(-1.0, 1.0) == 0.0
    assert add(0.0, 0.0) == 0.0


def test_subtract() -> None:
    """Testuje poprawność działania funkcji odejmowania."""
    assert subtract(5.0, 3.0) == 2.0
    assert subtract(1.0, 1.0) == 0.0
    assert subtract(0.0, 5.0) == -5.0
