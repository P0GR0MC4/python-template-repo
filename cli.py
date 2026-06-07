import sys
from logic.calculator import add, subtract


def main() -> None:
    """Główna funkcja sterująca działaniem kalkulatora w konsoli."""
    print("=== Prosty Kalkulator CLI ===")
    try:
        x = float(input("Podaj pierwszą liczbę: "))
        y = float(input("Podaj drugą liczbę: "))
    except ValueError:
        print("Błąd: Wprowadzona wartość musi być liczbą!")
        sys.exit(1)

    print(f"Wynik dodawania: {add(x, y)}")
    print(f"Wynik odejmowania: {subtract(x, y)}")


if __name__ == "__main__":
    main()
