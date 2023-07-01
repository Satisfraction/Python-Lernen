# Füge hier die Imports laut README.md hinzu
import pickle
import os 

# Importiere das datetime-Modul, um Zeitstempel zu generieren
import datetime

# Erstelle eine leere Liste für die To-Do-Liste
todo_list = []

# Fülle die Lücken entsprechend der Anweisung in der README.md

# Erstelle eine Funktion zur Hinzufügung von Aufgaben
def add_task():
    # Fordere den Benutzer auf, eine Aufgabe einzugeben
    task = input("Gib eine Aufgabe ein: ")
    # Gib die eingegebene Aufgabe zurück
    return task

# Erstelle eine Funktion zum Anzeigen der To-Do-Liste
def show_todo_list():
    # Gib eine Überschrift aus
    print("To-Do-Liste:")
    # Gehe durch die To-Do-Liste und gib jede Aufgabe und ihren Zeitstempel aus
    for i, task in enumerate(todo_list):
        task_name, timestamp = task
        print(f"{i + 1}. {task_name} - {timestamp}")

# Erstelle eine Funktion zum Markieren einer Aufgabe als erledigt
def mark_task_completed():
    # Zeige die To-Do-Liste an
    show_todo_list()
    # Fordere den Benutzer auf, die Aufgabe, die als erledigt markiert werden soll, auszuwählen
    task_index = int(input("Welche Aufgabe möchtest du als erledigt markieren? (Gib die Nummer ein): "))
    # Überprüfe, ob die ausgewählte Aufgabe gültig ist und entferne sie aus der To-Do-Liste
    if 1 <= task_index <= len(todo_list):
        completed_task = todo_list.pop(task_index - 1)
        print(f"Aufgabe '{completed_task[0]}' wurde als erledigt markiert und von der Liste entfernt.")
    # Wenn die ausgewählte Aufgabe ungültig ist, gib eine Fehlermeldung aus
    else:
        print("Ungültige Aufgabennummer.")

# Führe den folgenden Code aus, wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    # Laden der To-Do-Liste beim Start des Programms
    # Füge hier den Code zum Laden der To-Do-Liste hinzu

    # Füge dem Benutzer so lange Aufgaben hinzu, bis er "Nein" sagt
    while True:
        action = input("Möchtest du eine Aufgabe hinzufügen? (Ja/Nein): ")
        if action.lower() != "ja":
            break
        task = add_task()
        # Füge die neue Aufgabe und den Zeitstempel der To-Do-Liste hinzu
        todo_list.append((task, datetime.datetime.now()))
        print(f"Aufgabe '{task}' wurde zur To-Do-Liste hinzugefügt.")

    # Markiere eine Aufgabe als erledigt
    while True:
        mark_task_completed()

        if len(todo_list) == 0:
            print("Die To-Do-Liste ist leer.")
            break
        else:
            action = input("Möchtest du eine weitere Aufgabe als erledigt markieren? (Ja/Nein): ")
            if action.lower() != "ja":
                break

    # Speichern der To-Do-Liste beim Beenden des Programms
    # Füge hier den Code zum Speichern der To-Do-Liste hinzu

    # Füge hier den code zum Automatischen Speichern der To-Do-Liste hinzu

    print("Das Programm wurde beendet. Die To-Do-Liste wurde gespeichert.")
