# Tutorial für den Code "letterCounter.py"

## Schritt 1: 

Öffnen Sie Ihren bevorzugten Texteditor oder eine integrierte Entwicklungsumgebung (IDE), um den Code einzugeben.

## Schritt 2: 

Erstellen Sie eine neue Datei mit dem Namen "letterCounter.py" oder nutzen Sie die Vorlage. 

- Fügen Sie den folgenden Code ein:

    ```python
    # Willkommensnachricht
    print("Willkommen zum ersten Miniprojekt! Ich bin eine Anwendung, die eine Nachricht und einen Buchstaben von dir annimmt. Meine Aufgabe ist es, zu zählen, wie oft dieser Buchstabe in der Nachricht vorkommt und seinen Prozentsatz zu berechnen.")

Dieser Code gibt eine Willkommensnachricht aus, um den Benutzer über die Funktionalität der Anwendung zu informieren.

## Schritt 3: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Abrufen der Benutzereingaben
    user_message = input("Bitte geben Sie Ihre Nachricht ein: ")
    user_letter = input("Bitte geben Sie Ihren Buchstaben ein: ")

Diese beiden Zeilen fordern den Benutzer auf, eine Nachricht und einen Buchstaben einzugeben, die in der Nachricht gezählt werden sollen. Die Eingaben des Benutzers werden in den Variablen `user_message` und `user_letter` gespeichert.

## Schritt 4: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Ausgeben der Benutzereingaben
    print(user_message)
    print(user_letter)

Diese beiden Zeilen geben die eingegebene Nachricht und den eingegebenen Buchstaben auf dem Bildschirm aus, um dem Benutzer zu bestätigen, dass die Eingaben korrekt erfasst wurden.

## Schritt 5: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Zählt die Anzahl der Vorkommen des Buchstabens in der Nachricht.
    count = user_message.count(user_letter)

Diese Zeile verwendet die `count()`-Methode, um die Anzahl der Vorkommnisse des eingegebenen Buchstabens `user_letter` in der eingegebenen Nachricht `user_message` zu ermitteln. Das Ergebnis wird in der Variable `count` gespeichert.

## Schritt 6: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Berechne den Prozentsatz des Vorkommens des Buchstabens in der Nachricht.
    percentage = count / len(user_message) * 100

Diese Zeile berechnet den Prozentsatz der Vorkommnisse des Buchstabens in der Nachricht. Zuerst wird die Anzahl der Vorkommnisse `count` durch die Gesamtlänge der Nachricht `len(user_message)` geteilt. Dann wird das Ergebnis mit 100 multipliziert, um den Prozentsatz zu erhalten. Das Ergebnis wird in der Variable `percentage` gespeichert.

## Schritt 7: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Gibt die Ergebnisse aus
    print("Der Buchstabe", user_letter, "kommt", count, "mal in der Nachricht vor.")
    print("Der Prozentsatz des Vorkommens des Buchstabens", user_letter, "in der Nachricht ist", percentage, "%.")

Diese beiden Zeilen geben die Ergebnisse auf dem Bildschirm aus. Sie zeigen die Anzahl der Vorkommnisse des Buchstabens in der Nachricht sowie den berechneten Prozentsatz.

## Schritt 8: 

- Speichern Sie die Datei.

## Schritt 9: 

- Öffnen Sie Ihre Kommandozeile oder Ihr Terminal und navigieren Sie zum Speicherort der "letterCounter.py"-Datei.

## Schritt 10: 

- Führen Sie den Code aus, indem Sie den Befehl `python letterCounter.py` in der Kommandozeile oder im Terminal eingeben.

## Schritt 11: 

- Die Anwendung wird Sie begrüßen und nach Ihrer Nachricht und Ihrem Buchstaben fragen. 
- Geben Sie die entsprechenden Eingaben ein und drücken Sie die Eingabetaste.

## Schritt 12: 

- Die Anwendung gibt die eingegebene Nachricht und den Buchstaben aus.

## Schritt 13: 

- Die Anwendung zählt die Anzahl der Vorkommnisse des Buchstabens in der Nachricht und berechnet den Prozentsatz.

## Schritt 14: 

- Die Anwendung gibt die Ergebnisse aus, einschließlich der Anzahl der Vorkommnisse und des Prozentsatzes.


Herzlichen Glückwunsch! Sie haben erfolgreich den Code "letterCounter.py" erstellt und ausgeführt. Dieser Code ermöglicht es Benutzern, die Anzahl der Vorkommnisse eines bestimmten Buchstabens in einer Nachricht zu zählen und den Prozentsatz der Vorkommnisse zu berechnen.

Versuhen Sie gerne den Code zu erweitern und neue Funktionen hinzu zufügen. Viel Spaß beim Ausprobieren.