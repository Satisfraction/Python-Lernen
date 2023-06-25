# Fülle die Lücken entsprechend der Anweisung in der README.md

import ___

todo_list = []

def ___():
    task = input("Gib eine Aufgabe ein: ")
    ___

if __name__ == "___":
    while True:
        ___ = add_task()
        todo_list.append((___, ___.datetime.now()))
        ___(f"Aufgabe '{task}' wurde zur To-Do-Liste hinzugefügt.")

        action = input("Möchtest du eine weitere Aufgabe hinzufügen? (Ja/Nein): ")
        if action.lower() != "ja":
            ___
