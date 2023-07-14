# Tutorial für den Code "letterCounter.py" mit GUI (Benutzeroberfläche)

Ich empfehle vorher das CLI-Tutorial zu machen.
[CLI-Tutorial](https://github.com/Satisfraction/Python-Lernen/tree/main/mini-projekte/Buchstaben%20Z%C3%A4hler%20-%20Letter%20Counter/Buchstaben%20Z%C3%A4hler%20(Deutsch)/CLI-Tutorial%20(einfach))

## Schritt 1: 

- Öffnen Sie Ihren bevorzugten Texteditor oder eine integrierte Entwicklungsumgebung (IDE) und erstellen Sie eine neue Datei mit dem Namen "letterCounter.py" oder nutzen Sie die Vorlage.

## Schritt 2: 

- Fügen Sie die folgenden Zeilen Code hinzu:

    ```python
    # Importe
    import tkinter as tk
    from tkinter import messagebox

Diese Zeilen importieren das Tkinter-Modul, das für die Erstellung der grafischen Benutzeroberfläche (GUI) verwendet wird, und die `messagebox`-Klasse, die zur Anzeige von Meldungen verwendet wird.

## Schritt 3: 

- Fügen Sie die folgenden Zeilen Code hinzu:

    ```python
    # Funktion zum Berechnen der Anzahl und des Prozentwertes des Buchstabens
    def calculate_percentage():
        user_message = message_entry.get("1.0", tk.END).strip()
        user_letter = letter_entry.get()

        count = user_message.count(user_letter)
        percentage = count / len(user_message) * 100

        messagebox.showinfo("Ergebniss", f"Der Buchstabe {user_letter} kam {count} Mal in der Nachricht vor.\n\nDer Prozentsatz des Vorkommens des Buchstabens  {user_letter} in der Nachricht beträgt  {percentage:.2f}%.")

Diese Funktion `calculate_percentage()` wird aufgerufen, wenn der Benutzer auf die "Calculate"-Schaltfläche klickt. Sie ruft den eingegebenen Text aus dem Nachrichtenfeld `message_entry` ab, entfernt überflüssige Leerzeichen und speichert ihn in der Variable `user_message`. Der eingegebene Buchstabe wird aus dem Buchstabenfeld `letter_entry` abgerufen und in der Variable `user_letter` gespeichert.

Die Anzahl der Vorkommnisse des Buchstabens in der Nachricht wird mit der `count()`-Methode ermittelt und in der Variable `count` gespeichert. Der Prozentsatz wird berechnet, indem die Anzahl der Vorkommnisse durch die Gesamtlänge der Nachricht dividiert und mit 100 multipliziert wird. Das Ergebnis wird in der Variable `percentage` gespeichert.

Schließlich wird eine Meldung mit den Ergebnissen angezeigt, indem die `showinfo()`-Methode der `messagebox`-Klasse verwendet wird. Die Meldung enthält die Anzahl der Vorkommnisse und den Prozentsatz.

## Schritt 4: 

- Fügen Sie die folgenden Zeilen Code hinzu:

    ```python
    # Erstellen des GUI-Fenster
    window = tk.Tk()
    window.title("Buchstaben Zähler")
    window.geometry("400x300")

Diese Zeilen erstellen ein Fenster für die GUI-Anwendung mit dem Titel "Buchstaben Zähler" und einer Größe von 400x300 Pixeln.

## Schritt 5: 

- Fügen Sie die folgenden Zeilen Code hinzu:

    ```python
    # Erstellen der Textfelder und Label
    message_label = tk.Label(window, text="Nachricht:")
    message_label.pack()
    message_entry = tk.Text(window, width=50, height=10)
    message_entry.pack()

    letter_label = tk.Label(window, text="Buchstabe:")
    letter_label.pack()
    letter_entry = tk.Entry(window)
    letter_entry.pack()

Diese Zeilen erstellen Beschriftungen (Labels) und Eingabefelder (Textfeld und Einzelfeld) für die Nachricht und den Buchstaben in der GUI. Die `Label`-Klasse wird verwendet, um Textbeschriftungen zu erstellen, während die `Text`- und `Entry`- Klassen Eingabefelder für mehrzeiligen Text bzw. einen einzelnen Text ermöglichen.

## Schritt 6: 

- Fügen Sie die folgenden Zeilen Code hinzu:

    ```python
    # Erstellen des Berechnen Buttons
    calculate_button = tk.Button(window, text="Berechnen", command=calculate_percentage)
    calculate_button.pack()

Diese Zeilen erstellen eine Schaltfläche mit dem Text "Berechnen" in der GUI. Beim Klicken auf die Schaltfläche wird die Funktion `calculate_percentage()` aufgerufen.

## Schritt 7: 

- Fügen Sie die folgende Zeile Code hinzu:

    ```python
    # Starten des GUI main loop
    window.mainloop()

Diese Zeile startet die Hauptschleife der GUI-Anwendung und ermöglicht die Interaktion mit dem Benutzer.

## Schritt 8: 

- Speichern Sie die Datei.

## Schritt 9: 

- Öffnen Sie Ihre Kommandozeile oder Ihr Terminal und navigieren Sie zum Speicherort der "letterCounter.py"-Datei.

## Schritt 10: 

- Führen Sie den Code aus, indem Sie den Befehl `python letterCounter.py` in der Kommandozeile oder im Terminal eingeben.

## Schritt 11: 

- Das GUI-Fenster der Anwendung wird geöffnet.

## Schritt 12: 

- Geben Sie eine Nachricht in das Nachrichtenfeld ein und geben Sie den Buchstaben ein, nach dem gesucht werden soll.

## Schritt 13: 

- Klicken Sie auf die Schaltfläche "Berechnen".

## Schritt 14: 

- Eine Meldungsfeld wird angezeigt, das die Ergebnisse anzeigt. Es zeigt die Anzahl der Vorkommnisse des Buchstabens in der Nachricht sowie den berechneten Prozentsatz.

## Schritt 15: 

- Klicken Sie auf "OK" oder schließen Sie das Meldungsfeld, um fortzufahren.

Herzlichen Glückwunsch! Sie haben erfolgreich den Code "letterCounter.py" erstellt und ausgeführt. Diese Anwendung ermöglicht es Benutzern, die Anzahl der Vorkommnisse eines bestimmten Buchstabens in einer Nachricht zu zählen und den Prozentsatz der Vorkommnisse in einer einfachen GUI anzuzeigen.

Versuhen Sie gerne den Code zu erweitern und neue Funktionen hinzu zufügen. Viel Spaß beim Ausprobieren.