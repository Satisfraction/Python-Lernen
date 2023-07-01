# Schritt 5: Speichern und Wiederherstellen der To-Do-Liste

In diesem Schritt werden wir die Funktionalität hinzufügen, um die To-Do-Liste zu speichern und wiederherzustellen, damit der Benutzer seine Aufgaben auch nach dem Beenden des Programms behalten kann.

## Anleitung

1. Füge am Anfang der Datei `todo_list.py` den folgenden Code hinzu, um die Module `pickle` und `os` zu importieren:

   ```python
   import pickle
   import os

2. Füge an den enstprechenden Stellen der Datei den folgenden Code hinzu, um die Funktionen zum Speichern und Wiederherstellen der To-Do-Liste zu implementieren:

- Funktion zum Speichern:

    ```python
    def save_todo_list():
        with open("todo_list.pickle", "wb") as file:
            pickle.dump(todo_list, file)

- Funktion zum Laden:

    ```python
    def load_todo_list():
        if os.path.exists("todo_list.pickle"):
            with open("todo_list.pickle", "rb") as file:
                return pickle.load(file)
        else:
            return []

    todo_list = load_todo_list()

- Funktion zum Automatischne Speichern beim beenden des Programms:

    ```python
    def exit_program():
        save_todo_list()
        print("Das Programm wurde beendet. Die To-Do-Liste wurde gespeichert.")

    import atexit
    atexit.register(exit_program)

Mit diesen Änderungen wird die To-Do-Liste automatisch beim Beenden des Programms gespeichert und beim nächsten Start wiederhergestellt. Dadurch geht die Liste nicht verloren und der Benutzer kann seine Aufgaben über mehrere Sitzungen hinweg verwalten.

Stelle sicher, dass du die Schritte korrekt befolgst und speichere deine Änderungen.