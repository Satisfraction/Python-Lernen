# Schritt 6 Grafische Benutzeroberfläche (GUI)

![To-Do-List App Preview](preview.png)

## 1: Importieren der erforderlichen Module

- Importe:

    ```python
    import tkinter as tk
    import pickle
    import os
    import datetime

In diesem Schritt importieren wir die benötigten Module für die Erstellung der GUI, das Speichern und Laden der To-Do-Liste sowie die Bearbeitung von Datums- und Zeitinformationen.

## 2: Laden der To-Do-Liste

- funktion zum Laden:

    ```python
    def load_todo_list():
        if os.path.exists("todo_list.pickle"):
            with open("todo_list.pickle", "rb") as file:
                return pickle.load(file)
        else:
            return []

Wir definieren eine Funktion load_todo_list(), die überprüft, ob eine gespeicherte To-Do-Liste existiert. Falls ja, wird sie aus der Datei todo_list.pickle geladen und zurückgegeben. Andernfalls wird eine leere Liste zurückgegeben.

## 3: Speichern der To-Do-Liste

- Funktion zum Speichern:

    ```python
    def save_todo_list():
        with open("todo_list.pickle", "wb") as file:
            pickle.dump(todo_list, file)

Wir definieren eine Funktion save_todo_list(), die die aktuelle To-Do-Liste in der Datei "todo_list.pickle" speichert.

## 4: Markieren einer Aufgabe als erledigt

- Funktion zum Markieren einer Aufgabe als erledigt:

    ```python
    def mark_task_completed():
        selected_index = listbox.curselection()
        if selected_index:
            index = selected_index[0]
            completed_task = todo_list.pop(index)
            listbox.delete(index)
            save_todo_list()
            print(f"Aufgabe '{completed_task[0]}' wurde als erledigt markiert und von der Liste entfernt.")
        else:
            print("Keine Aufgabe ausgewählt.")

Wir definieren eine Funktion mark_task_completed(), die die ausgewählte Aufgabe in der GUI als erledigt markiert. Dabei wird die Aufgabe aus der To-Do-Liste entfernt, die Listbox aktualisiert und die Liste gespeichert.

## 5: Hinzufügen einer Aufgabe

- Funktion zum hinzufügen von Aufgaben:

    ```python
    def add_task():
        task = entry.get()
        if task:
            todo_list.append((task, datetime.datetime.now()))
            listbox.insert(tk.END, task)
            save_todo_list()
            entry.delete(0, tk.END)

Wir definieren eine Funktion add_task(), um eine neue Aufgabe zur To-Do-Liste hinzuzufügen. Dabei wird der aktuelle Zeitstempel verwendet, um das Hinzufüge-Datum festzuhalten. Die Aufgabe wird der Liste hinzugefügt, die Listbox aktualisiert, die Liste gespeichert und das Eingabefeld geleert.

## 6: Erstellen der Benutzeroberfläche

- Funktion zum Öffnen der Benutzeroberfläche:

    ```python
    def open_ui():
        global todo_list, listbox, entry
        root = tk.Tk()
        root.title("To-Do-Liste")


- Funktion zum Laden der To-Do-Liste:

    ```python
    # Laden der To-Do-Liste
    todo_list = load_todo_list()


- Funktion für das erstellen der Listbox:

    ```python
    # Erstellen der Listbox
    listbox = tk.Listbox(root, width=50)
    listbox.pack(pady=10)


- Funktion für das Hinzufügen der Vorhandenen Aufgaben:

    ```python
    # Hinzufügen der vorhandenen Aufgaben zur Listbox
    for task in todo_list:
        listbox.insert(tk.END, task[0])


- Erstellung des Eingabefeldes

    ```python
    # Erstellen des Eingabefelds und der Schaltfläche zum Hinzufügen von Aufgaben
    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)
    add_button = tk.Button(root, text="Aufgabe hinzufügen", command=add_task)
    add_button.pack(pady=5)


- Erstellung der Schaltfläche zum erledigt Markieren:

    ```python
    # Erstellen der Schaltfläche zum Markieren einer Aufgabe als erledigt
    mark_button = tk.Button(root, text="Aufgabe erledigt", command=mark_task_completed)
    mark_button.pack(pady=5)


- Funktion zum Schließen der GUI und Speichern der Liste:

    ```python
    # Schließen der GUI und Speichern der Liste beim Beenden des Programms
    def exit_program():
        save_todo_list()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", exit_program)


- Befehl zum starten der Hauptschleife:

    ```python
    # Start der Hauptschleife der Benutzeroberfläche
    root.mainloop()

Wir definieren eine Funktion open_ui(), um die Benutzeroberfläche zu erstellen und anzuzeigen. In dieser Funktion werden die Listbox, das Eingabefeld und die Schaltflächen für das Hinzufügen und Markieren von Aufgaben erstellt. Außerdem wird die To-Do-Liste geladen, bereits vorhandene Aufgaben werden zur Listbox hinzugefügt, und die Listbox wird angezeigt. Beim Schließen der GUI wird die Liste gespeichert.

## 7: Ausführen der Anwendung

- Codeblock zum Ausführen der Anwendung:

    ```python
    if __name__ == "__main__":
        todo_list = []
        listbox = None
        entry = None
        open_ui()

Am Ende des Codes wird überprüft, ob das Skript direkt ausgeführt wird. In diesem Fall werden die Variablen initialisiert und die Funktion open_ui() aufgerufen, um die Anwendung zu starten.

Stelle sicher, dass du die Schritte korrekt befolgst und speichere deine Änderungen.
