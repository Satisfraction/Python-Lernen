# Schritt 3: Projektstruktur und User Input - Aufgaben hinzufügen

In diesem Schritt werden wir die grundlegende Projektstruktur erstellen und die Benutzereingabe implementieren, um Aufgaben zur To-Do-Liste hinzuzufügen.

## Anleitung

1. Erstelle im Projektverzeichnis eine neue Datei mit dem Namen `todo_list.py`.

2. Definiere die grundlegende Struktur des Projekts:

   ```python
   import datetime

   todo_list = []

3. Implementiere die Funktion zur Benutzereingabe:

    ```python
    def add_task():
        task = input("Gib eine Aufgabe ein: ")
        return task

4. Füge den Code hinzu, um das Programm auszuführen:

    ```python
    if __name__ == "__main__":
        while True:
            task = add_task()
            todo_list.append((task, datetime.datetime.now()))
            print(f"Aufgabe '{task}' wurde zur To-Do-Liste hinzugefügt.")

            action = input("Möchtest du eine weitere Aufgabe hinzufügen? (Ja/Nein): ")
            if action.lower() != "ja":
                break

Dieser Code erstellt eine Endlosschleife, die den Benutzer wiederholt nach Aufgaben fragt. Jede eingegebene Aufgabe wird der To-Do-Liste zusammen mit dem aktuellen Datum und der Uhrzeit hinzugefügt. Der Benutzer kann das Programm beenden, indem er "Nein" eingibt.

5. Speichere die Datei und führe das Programm aus. Achte dabei darauf das du dich im richtigen Dateipfad befindest.

   ```python
   python todo_list.py

Jetzt hast du eine grundlegende Projektstruktur und die Benutzereingabe implementiert, um Aufgaben zur To-Do-Liste hinzuzufügen.
