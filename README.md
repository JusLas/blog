# Moduł 16

## Projekt końcowy

Aplikacja blog.

### Instalacja i uruchomienie

1. Pobranie kodu źródłowego

2. [Instalacja i uruchomienie środowiska wirtalnego](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

    _Dalsza interakcja powinna się odbywać przy aktywowanym środowisku
    wirtualnym dedykowanym dla projektu_

3. Instalacja bibliotek python:

    `pip install -r requirements.txt`

3. Inicjalizacja zmiennych środowiskowych

    `set FLASK_APP=blog`

4. Inicjalizacja bazy danych

    `flask db init`

5. Wykonanie migracji

    `flask db upgrade`

6. Uruchomienie serwera lokalnego

    `flask run`

### Zadania

1. [Zadanie: refactoring](https://github.com/JusLas/blog/commit/ef2798b22db883223fd3129400a0e6712d2cde36)

2. Zadanie: chwalimy się projektem!:

    1. [Commit](https://github.com/JusLas/blog/commit/053bca0b72555ead4f5b329a3fab3884ad06476f)
    2. [Opublikowana aplikacja](https://jmlaszuk-blog.herokuapp.com/)