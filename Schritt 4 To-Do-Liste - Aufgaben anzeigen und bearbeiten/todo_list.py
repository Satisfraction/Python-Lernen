# Importiere das datetime-Modul, um Zeitstempel zu generieren
import datetime

# Erstelle eine leere Liste für die To-Do-Liste
todo_list = []


# Fülle die Lücken entsprechend der Anweisung in der README.md

# Erstelle eine Funktion zur Hinzufügung von Aufgaben
def ___():
    # Fordere den Benutzer auf, eine Aufgabe einzugeben
    ___ = input("Gib eine Aufgabe ein: ")
    # Gib die eingegebene Aufgabe zurück
    return task

# Erstelle eine Funktion zum Anzeigen der To-Do-Liste
def ____():
    # Gib eine Überschrift aus
    ____("To-Do-Liste:")
    # Gehe durch die To-Do-Liste und gib jede Aufgabe und ihren Zeitstempel aus
    for i, ___ in enumerate(todo_list):
        task_name, timestamp = ____
        print(f"{i + 1}. {task_name} - {____}")

# Erstelle eine Funktion zum Markieren einer Aufgabe als erledigt
def ____():
    # Zeige die To-Do-Liste an
    ____()
    # Fordere den Benutzer auf, die Aufgabe, die als erledigt markiert werden soll, auszuwählen
    ____ = int(input("Welche Aufgabe möchtest du als erledigt markieren? (Gib die Nummer ein): "))
    # Überprüfe, ob die ausgewählte Aufgabe gültig ist und entferne sie aus der To-Do-Liste
    if 1 <= task_index <= len(____):
        ____ = todo_list.pop(task_index - 1)
        print(f"Aufgabe '{___[0]}' wurde als erledigt markiert und von der Liste entfernt.")
    # Wenn die ausgewählte Aufgabe ungültig ist, gib eine Fehlermeldung aus
    else:
        ____("Ungültige Aufgabennummer.")

# Führe den folgenden Code aus, wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    # Füge dem Benutzer so lange Aufgaben hinzu, bis er "Nein" sagt
    while True:
        action = ____("Möchtest du eine Aufgabe hinzufügen? (Ja/Nein): ")
        if action.lower() != "ja":
            ____
        task = ____()
        # Füge die neue Aufgabe und den Zeitstempel der To-Do-Liste hinzu
        ____.append((task, datetime.datetime.now()))
        print(f"Aufgabe '{____}' wurde zur To-Do-Liste hinzugefügt.")

    # Markiere eine Aufgabe als erledigt
    ____()   # Bonus Fortsetzung ab hier
