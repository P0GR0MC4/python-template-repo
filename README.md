Projekt: Automatyzacja Jakości Kodu w Pythonie

Projekt zawiera aplikację kalkulatora CLI wyposażoną w lokalne narzędzia do automatycznego formatowania, analizy statycznej (lintowania) oraz testowania kodu. W repozytorium skonfigurowano również potok Continuous Integration (CI) za pomocą GitHub Actions.

---

## Quick Start (Szybki start lokalny)

Aby uruchomić projekt na swoim komputerze (instrukcja dla systemu Windows / PowerShell):

1. **Utworzenie środowiska wirtualnego `venv` i instalacja zależności:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\pip install -r requirements.txt

2. **Uruchomienie aplikacji kalkulatora w konsoli:**
  .\venv\Scripts\python cli.py

3. **Instrukcja uruchamiania lintera i testów**
Formatowanie kodu (Black)
  .\venv\Scripts\black cli.py logic tests

Sprawdzanie formatowania (bez modyfikacji plików)
  .\venv\Scripts\black --check cli.py logic tests

Analiza statyczna kodu (Pylint)
  .\venv\Scripts\pylint cli.py logic tests

Uruchamianie testów jednostkowych (Pytest)
  .\venv\Scripts\pytest tests/
4. **Jak działa pipeline CI**
**Kiedy się uruchamia?**
Pipeline odpala się automatycznie na serwerach GitHub w dwóch przypadkach:
  - Przy każdym wykonaniu komendy git push na gałęzie: main, master lub develop.
  - Przy otwarciu lub zaktualizowaniu Pull Requestu (PR) do gałęzi main lub master.

**Co dokładnie sprawdza i wykonuje?**
  - Uruchamia czystą instancję systemu Ubuntu Linux i wykonuje kolejno kroki (wykorzystując skrypty z katalogu scripts/):
  - Weryfikuje środowiska: Pobiera kod z repozytorium i konfiguruje środowisko Python 3.12.
  - Budowanie i instalacja: Uruchamia scripts/create_venv.sh, tworząc izolowane środowisko i instalując pakiety z requirements.txt.
  - Format check: Wykonuje scripts/format_check.sh. Jeśli kod nie był sformatowany narzędziem black, ten krok kończy się błędem i zatrzymuje pipeline.
  - Linting: Wykonuje scripts/lint.sh przy użyciu lintera pylint. Wykrywa błędy w składni i strukturze kodu.
  - Testy automatyczne: Wykonuje scripts/test.sh. Odpala pytest, upewniając się, czy żadna nowa zmiana nie popsuła logiki matematycznej kalkulatora.
