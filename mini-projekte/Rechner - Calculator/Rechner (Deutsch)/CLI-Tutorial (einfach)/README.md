# `rechner.py` Tutorial CLI-Version

## Schritt 1: 

- Öffnen Sie Ihren bevorzugten Texteditor oder eine integrierte Entwicklungsumgebung (IDE).

## Schritt 2: 

- Erstellen Sie eine neue Datei und speichern Sie sie als `rechner.py` oder nutzen Sie die Vorlage.

## Schritt 3: 

- Fügen Sie den folgenden Code in die `rechner.py`-Datei ein:

    ```python
    # Dies ist ein einfaches Taschenrechnerprogramm.

    # Funktion zum Addieren zweier Zahlen
    def add(num1, num2):
        return num1 + num2

    # Funktion zum Subtrahieren zweier Zahlen
    def subtract(num1, num2):
        return num1 - num2

    # Funktion zum Multiplizieren zweier Zahlen
    def multiply(num1, num2):
        return num1 * num2

    # Funktion zum Dividieren zweier Zahlen, behandelt die Division durch Null
    def divide(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

    # Druckt den Titel des Rechners
    print("Einfacher Taschenrechner")
    print("------------------")


### Erklärung:

- Der obere Teil des Codes definiert vier Funktionen: `add`, `subtract`, `multiply` und `divide`, um die Addition, Subtraktion, Multiplikation und Division von Zahlen durchzuführen.
- Jede Funktion nimmt zwei Argumente (`num1` und `num2`) entgegen und gibt das result der entsprechenden Operation zurück.
- Die `add`-Funktion addiert `num1` und `num2`, die `subtract`-Funktion subtrahiert `num2` von `num1`, die `multiply`-Funktion multipliziert `num1` und `num2`, und die `divide`-Funktion teilt `num1` durch `num2`.
- Die `divide`-Funktion enthält auch eine Bedingung, die prüft, ob `num2` nicht gleich 0 ist, um eine Division durch Null zu verhindern. Wenn `num2` 0 ist, wird die Fehlermeldung "Error: Division by zero" zurückgegeben.

## Schritt 4: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Start einer Endlosschleife für Benutzerinteraktion
    while True:
        # Druckt die verfügbaren Operationen
        print("Operation auswählen:")
        print("1. Addieren")
        print("2. Subtrahieren")
        print("3. Multiplizieren")
        print("4. Dividieren")
        print("5. Beenden")


### Erklärung:

- Diese Zeilen erstellen eine Endlosschleife, die die Benutzerinteraktion ermöglicht. Der Code wird wiederholt ausgeführt, bis der Benutzer das Programm beendet.
- Innerhalb der Schleife werden die verfügbaren Operationen auf dem Bildschirm angezeigt.

## Schritt 5: 

- Fügen Sie den folgenden Code hinzu:

    ```python
        # Aufforderung an den Benutzer, seine Wahl zu treffen
        choice = input("Geben Sie eine Auswahl (1-5) ein: ")


### Erklärung:

- Diese Zeile fordert den Benutzer auf, seine Wahl einzugeben, indem er eine Nummer von 1 bis 5 eingibt.

## Schritt 6: 

- Fügen Sie den folgenden Code hinzu:

    ```python
        # Prüfen, ob der Benutzer aussteigen will
        if choice == '5':
            print("Auf Wiedersehen!")
            break


### Erklärung:

- Diese Zeilen prüfen, ob der Benutzer die Option "Exit" ausgewählt hat.
- Wenn der Benutzer '5' eingibt, wird die Nachricht "Goodbye!" ausgegeben und die Schleife mit `break` beendet.

## Schritt 7: 

- Fügen Sie den folgenden Code hinzu:

    ```python
        # Aufforderung an den Benutzer, die beiden Zahlen einzugeben
        num1 = float(input("Geben Sie die erste Zahl ein: "))
        num2 = float(input("Geben Sie die zweite Zahl ein: "))


### Erklärung:

- Diese Zeilen fordern den Benutzer auf, die beiden Zahlen einzugeben, auf die die ausgewählte Operation angewendet werden soll.
- Die `float()`-Funktion wird verwendet, um sicherzustellen, dass die eingegebenen Werte als Gleitkommazahlen interpretiert werden.

## Schritt 8: 

- Fügen Sie den folgenden Code hinzu:

    ```python
        # Ausführen der ausgewählten Operation basierend auf der Wahl des Benutzers
        if choice == '1':
            result = add(num1, num2)
            print(f "Die Summe von {num1} und {num2} ist {result}")
        elif choice == '2':
            result = Subtraktion(num1, num2)
            print(f "Die Differenz zwischen {num1} und {num2} ist {result}")
        elif choice == '3':
            result = Multiplikation(num1, num2)
            print(f "Das Produkt von {num1} und {num2} ist {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f "Die Division von {num1} durch {num2} ist {result}")
        else:
            print("Ungültige Eingabe, bitte versuchen Sie es erneut.")


### Erklärung:

- Diese Zeilen führen die ausgewählte Operation basierend auf der Benutzerwahl aus.
- Die `if-elif-else`-Anweisungen überprüfen den Wert der `choice`-Variablen und rufen die entsprechende Funktion auf (add, subtract, multiply oder divide).
- Das result der Operation wird in der Variablen `result` gespeichert und zusammen mit den eingegebenen Zahlen auf dem Bildschirm ausgegeben.
- Wenn der Benutzer eine ungültige Eingabe macht (keine Zahl zwischen 1 und 5), wird die Meldung "Invalid input. Please try again." ausgegeben.

## Schritt 9: 

- Fügen Sie den folgenden Code hinzu:

    ```python
        print("Invalid input. Please try again.")


### Erklärung:

- Diese Zeile gibt eine Meldung aus, wenn der Benutzer eine ungültige Eingabe für die Optionen gemacht hat.

## Schritt 10: 

- Speichern Sie die Datei.

## Schritt 11: 

- Öffnen Sie Ihre Kommandozeile oder Ihr Terminal und navigieren Sie zum Speicherort der `rechner.py`-Datei.

## Schritt 12: 

- Führen Sie den Code aus, indem Sie den Befehl `python rechner.py` in der Kommandozeile oder im Terminal eingeben.

## Schritt 13: 

- Die Titelzeile des Taschenrechners "Simple Calculator" wird auf dem Bildschirm angezeigt.

## Schritt 14: 

- Das Programm bietet eine Liste der verfügbaren Operationen an und fordert den Benutzer auf, eine Wahl zu treffen.

## Schritt 15: 

- Geben Sie eine Zahl von 1 bis 5 ein, um die gewünschte Operation auszuwählen.

## Schritt 16: 

- Wenn Sie '5' eingeben, wird das Programm beendet und die Nachricht "Goodbye!" wird angezeigt.

## Schritt 17: 

- Für die anderen Optionen fordert das Programm den Benutzer auf, die beiden Zahlen einzugeben, auf die die Operation angewendet werden soll.

## Schritt 18: 

- Das Programm führt die ausgewählte Operation aus und gibt das result auf dem Bildschirm aus.

## Schritt 19: 

- Das Programm kehrt zum Menü zurück und fordert den Benutzer erneut auf, eine Operation auszuwählen.


Herzlichen Glückwunsch! Sie haben erfolgreich den Code `rechner.py` erstellt und ausgeführt. Dieses einfache Taschenrechnerprogramm ermöglicht es dem Benutzer, verschiedene mathematische Operationen auszuwählen und auf zwei Zahlen anzuwenden.