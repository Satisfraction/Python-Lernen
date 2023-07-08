# `rechner.py` Tutorial GUI-Version

## Schritt 1: 

- Öffnen Sie Ihren bevorzugten Texteditor oder eine integrierte Entwicklungsumgebung (IDE).

## Schritt 2: 

- Erstellen Sie eine neue Datei und speichern Sie sie als `rechner.py` oder nutzen Sie die Vorlage.

## Schritt 3: 

- Fügen Sie den folgenden Code in die "rechner.py"-Datei ein:

    ```python
    # Importe
    import tkinter as tk

    # Ein neues Fenster erstellen
    window = tk.Tk()
    window.title("Einfacher Rechner")
    window.geometry("400x300")


### Erklärung:

- Die ersten Zeilen importieren das Tkinter-Modul, das zur Erstellung der grafischen Benutzeroberfläche (GUI) verwendet wird.
- Die nächsten Zeilen erstellen ein neues Fenster (`window`), setzen den Fenstertitel auf "Simple Calculator" und die Fenstergröße auf 400x300 Pixel.

## Schritt 4: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Funktion zur Durchführung der Addition
    def add():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 + num2
        result_label.config(text=f"Die Summe von {num1} und {num2} ist {result}")

    # Funktion zur Durchführung einer Subtraktion
    def subtract():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 - num2
        result_label.config(text=f"Die Differenz zwischen {num1} und {num2} ist {result}")

    # Funktion zur Durchführung der Multiplikation
    def multiply():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        result_label.config(text=f"Die Multiplikatin von {num1} und {num2} ist {result}")

    # Funktion zur Durchführung der Division
    def divide():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if num2 != 0:
            result = num1 / num2
            result_label.config(text=f"Die Division von {num1} durch {num2} ist {result}")
        else:
            result_label.config(text="Fehler: Division durch Null")


### Erklärung:

- Diese Zeilen definieren vier Funktionen (`add`, `subtract`, `multiply` und `divide`), die jeweils eine bestimmte mathematische Operation ausführen.
- Jede Funktion liest die eingegebenen Zahlen (`num1` und `num2`) aus den Eingabefeldern (`num1_entry` und `num2_entry`) und führt die entsprechende Operation aus.
- Das Ergebnis wird in der Variablen `result` gespeichert und in das Textfeld `result_label` geschrieben, um es anzuzeigen.

## Schritt 5: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Eingabefelder für Zahlen erstellen
    num1_entry = tk.Entry(window)
    num1_entry.pack()

    num2_entry = tk.Entry(window)
    num2_entry.pack()


### Erklärung:

- Diese Zeilen erstellen zwei Eingabefelder (`num1_entry` und `num2_entry`), in denen der Benutzer die Zahlen eingeben kann.
- Die `Entry`-Klasse aus Tkinter wird verwendet, um die Eingabefelder zu erstellen.
- Mit der `pack()`-Methode werden die Eingabefelder in das Fenster (`window`) platziert.

## Schritt 6: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Schaltflächen für Operationen erstellen
    add_button = tk.Button(window, text="Add", command=add)
    add_button.pack(padx=5, pady=5)

    subtract_button = tk.Button(window, text="Subtract", command=subtract)
    subtract_button.pack(padx=5, pady=5)

    multiply_button = tk.Button(window, text="Multiply", command=multiply)
    multiply_button.pack(padx=5, pady=5)

    divide_button = tk.Button(window, text="Divide", command=divide)
    divide_button.pack(padx=5, pady=5)


### Erklärung:

- Diese Zeilen erstellen vier Schaltflächen (`add_button`, `subtract_button`, `multiply_button` und `divide_button`), die den Benutzern ermöglichen, die entsprechenden Operationen auszuwählen.
- Jede Schaltfläche hat einen Text (z.B. "Add", "Subtract", usw.) und wird mit der entsprechenden Funktion (`add`, `subtract`, usw.) verknüpft.
- Mit der `pack()`-Methode werden die Schaltflächen in das Fenster (`window`) platziert.
- Die `command`-Parameter verweisen auf die entsprechenden Funktionen, die beim Klicken auf die Schaltflächen ausgeführt werden sollen.

## Schritt 7: 

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Erstellen Sie einen Labelrahmen für das Ergebnis.
    result_frame = tk.LabelFrame(window, text="Output", width=300, height=100)
    result_frame.pack(padx=10, pady=10)

    # Ein Label für das Ergebnis erstellen
    result_label = tk.Label(result_frame, text="")
    result_label.pack()


### Erklärung:

- Diese Zeilen erstellen einen Rahmen (`result_frame`), um das Ergebnis anzuzeigen, und ein Beschriftungsfeld (`result_label`), das das Ergebnis enthält.
- Der Rahmen wird mit dem Text "Output" erstellt und auf eine Breite von 300 Pixeln und eine Höhe von 100 Pixeln festgelegt.
- Der Rahmen wird mit der `pack()`-Methode in das Fenster (`window`) platziert.
- Das Beschriftungsfeld wird im Rahmen erstellt und zunächst leer gelassen.

## Schritt 8:

- Fügen Sie den folgenden Code hinzu:

    ```python
    # Start der Hauptereignisschleife
    window.mainloop()


### Erklärung:

- Diese Zeile startet die Hauptereignisschleife der GUI-Anwendung.
- Die Schleife läuft fortlaufend und ermöglicht dem Benutzer die Interaktion mit der Anwendung, bis das Fenster geschlossen wird.

## Schritt 9: 

- Speichern Sie die Datei.

## Schritt 10: 

- Öffnen Sie Ihre Kommandozeile oder Ihr Terminal und navigieren Sie zum Speicherort der "rechner.py"-Datei.

## Schritt 11: 

- Führen Sie den Code aus, indem Sie den Befehl `python rechner.py` in der Kommandozeile oder im Terminal eingeben.

## Schritt 12: 

- Das GUI-Fenster des Taschenrechners wird geöffnet.

## Schritt 13: 

- Geben Sie die Zahlen in die Eingabefelder ein, auf die die gewünschte Operation angewendet werden soll.

## Schritt 14: 

- Klicken Sie auf die entsprechende Schaltfläche (Add, Subtract, Multiply oder Divide), um die Operation auszuführen.

## Schritt 15: 

- Das Ergebnis wird im Beschriftungsfeld angezeigt.


Herzlichen Glückwunsch! Sie haben erfolgreich den Code `rechner.py` erstellt und ausgeführt. Dieses einfache Taschenrechnerprogramm ermöglicht es dem Benutzer, verschiedene mathematische Operationen auszuwählen und auf zwei Zahlen anzuwenden.