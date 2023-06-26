# Schritt 4: Anzeigen der To-Do-Liste und Aufgaben als erledigt markieren

In diesem Schritt werden wir die To-Do-Liste anzeigen und dem Benutzer ermöglichen, Aufgaben als erledigt zu markieren.

## Anleitung

1. Öffne die Datei `todo_list.py`.

2. Füge am Ende der Datei den folgenden Code hinzu, um die Funktionen zur Anzeige der To-Do-Liste und zum Markieren von Aufgaben als erledigt zu implementieren:

    1. erstelle die Funktion zum Anzeigen der To-Do-Liste:

        ```python
        def show_todo_list():
            print("To-Do-Liste:")
            for i, task in enumerate(todo_list):
                task_name, timestamp = task
                print(f"{i + 1}. {task_name} - {timestamp}")


    2. erstelle die Funktion zum Komplett Markieren:

        ```python
        def mark_task_completed():
            show_todo_list()
            task_index = int(input("Welche Aufgabe möchtest du als erledigt markieren? (Gib die Nummer ein): "))
            if 1 <= task_index <= len(todo_list):
                completed_task = todo_list.pop(task_index - 1)
                print(f"Aufgabe '{completed_task[0]}' wurde als erledigt markiert und von der Liste entfernt.")
            else:
                print("Ungültige Aufgabennummer.")

    3. Aktualisiere den Code zum Ausführen des Programs:

        ```python
        if __name__ == "__main__":
            while True:
                action = input("Möchtest du eine Aufgabe hinzufügen? (Ja/Nein): ")
                if action.lower() != "ja":
                    break
                task = add_task()
                todo_list.append((task, datetime.datetime.now()))
                print(f"Aufgabe '{task}' wurde zur To-Do-Liste hinzugefügt.")

            mark_task_completed()


3. Speichere die Datei und führe das Programm aus.

    ```python
    python todo_list.py

Nachdem du Aufgaben zur To-Do-Liste hinzugefügt hast, wird die To-Do-Liste angezeigt. Du wirst aufgefordert, die Nummer einer Aufgabe einzugeben, die du als erledigt markieren möchtest. Die ausgewählte Aufgabe wird als erledigt markiert und von der Liste entfernt und das Program wird beendet.

Jetzt kannst du die To-Do-Liste anzeigen und eine Aufgaben als erledigt markieren.

---------------------------------------------------------------------------------------------------------------

### Bonus 

Überprüfen ob mehrere Einträge in der To-Do-Liste vorhanden sind und die abfrage zum erledigt markieren fortsetzen bis die Liste leer ist.

1. Ergänze den Code zum Ausführen der Datei wiefolgt:

    ```python
    while True:
        mark_task_completed()

        if len(todo_list) == 0:
            print("Die To-Do-Liste ist leer.")
            break
        else:
            action = input("Möchtest du eine weitere Aufgabe als erledigt markieren? (Ja/Nein): ")
            if action.lower() != "ja":
                break
