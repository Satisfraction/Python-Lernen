# Fülle die Lücken entsprechend der Anweisung in der README.md

import ___      # hier importieren wir die datetime Funktion

todo_list = []      # hier definieren wir die Liste

def ___():
    task = input("Gib eine Aufgabe ein: ")      # hier wird die Aufgabe eingetragen mittels der input Funktion
    ___                                # hier wird die Aufgabe ausgegeben mittels return Funktion
if __name__ == "___":               
    while True:
        ___ = add_task()                    # hier rufen wir die add_task Funktion auf
        todo_list.append((___, ___.datetime.now()))      # hier wird die Aufgabe in der Liste hinzugefügt mittels der append Funktion
        ___(f"Aufgabe '{task}' wurde zur To-Do-Liste hinzugefügt.")      # hier wird die Aufgabe ausgegeben mittels der print Funktion

        action = input("Möchtest du eine weitere Aufgabe hinzufügen? (Ja/Nein): ")      # hier wird die Abfrage vom User geholt um Fortzusetzen mittels der input Funktion
        if action.lower() != "ja":                # hier wird das Programm abgebrochen, wenn die Abfrage nicht "Ja" ist
            ___
