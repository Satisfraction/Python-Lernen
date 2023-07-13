# Ergänze den Code an den entsprechenden Stellen nach der README.md Anleitung.

# Importe
import tkinter as tk
import pickle
import os
import datetime
# Import für die Kalenderauswahl hier einfügen

# Code für die Implementierung der verketteten Liste
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            count = 0
            while current and count != index:
                prev = current
                current = current.next
                count += 1
            if current:
                prev.next = current.next

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

# Laden der To-Do-Liste
def load_todo_list():
    if os.path.exists("todo_list.pickle"):
        with open("todo_list.pickle", "rb") as file:
            return pickle.load(file)
    else:
        return LinkedList()

# Speichern der To-Do-Liste
def save_todo_list():
    with open("todo_list.pickle", "wb") as file:
        pickle.dump(todo_list, file)

# Funktion zum Hinzufügen einer Aufgabe
def add_task():
    

# Funktion zum Sortieren der Aufgaben nach Aufgabentext
def sort_tasks_by_text():
    global todo_list
    sorted_list = sorted(todo_list, key=lambda x: x[0].lower())
    todo_list = LinkedList()
    for task in sorted_list:
        todo_list.append(task)
    refresh_listbox()

# Funktion zum Sortieren der Aufgaben nach Erstellungsdatum
def sort_tasks_by_date():
    global todo_list
    sorted_list = sorted(todo_list, key=lambda x: x[3])
    todo_list = LinkedList()
    for task in sorted_list:
        todo_list.append(task)
    refresh_listbox()

# Funktion zum Sortieren der Aufgaben nach Fälligkeitsdatum
def sort_tasks_by_due_date():
    

# Funktion zum Sortieren der Aufgaben nach Priorität
def sort_tasks_by_priority():
    

# Funktion zum Aktualisieren der Listbox
def refresh_listbox():
    

# Funktion zum Formatieren der Aufgabenanzeige in der Listbox
def format_task_display(task, priority, due_date, timestamp):
    return f"Task: {task} | Priority: {priority} | Due Date: {due_date} | Created: {timestamp}"

# Markieren einer Aufgabe als erledigt
def mark_task_completed():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        current = todo_list.head
        count = 0
        while current and count != index:
            current = current.next
            count += 1
        if current:
            completed_task = current.data[0]
            todo_list.remove(index)
            refresh_listbox()
            save_todo_list()
            print(f"Aufgabe '{completed_task}' wurde als erledigt markiert und von der Liste entfernt.")
    else:
        print("Keine Aufgabe ausgewählt.")

# Öffnen der Benutzeroberfläche
def open_ui():
    global todo_list, listbox, entry, priority_var, date_var
    root = tk.Tk()
    root.title("To-Do-Liste")

    # Laden der To-Do-Liste
    todo_list = load_todo_list()

    # Erstellen der Listbox
    listbox = tk.Listbox(root, width=80)
    listbox.pack(pady=10)

    # Hinzufügen der vorhandenen Aufgaben zur Listbox
    for task in todo_list:
        listbox.insert(tk.END, format_task_display(*task))

    # Erstellen des Eingabefelds für die Aufgabe
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    # Erstellen des Dropdown-Menüs für die Priorität
    

    # Erstellen der Kalenderauswahl für das Fälligkeitsdatum
    

    # Erstellen der Schaltfläche zum Hinzufügen von Aufgaben
    add_button = tk.Button(root, text="Aufgabe hinzufügen", command=add_task)
    add_button.pack(pady=5)

    # Erstellen der Schaltfläche zum Markieren einer Aufgabe als erledigt
    mark_button = tk.Button(root, text="Aufgabe erledigt", command=mark_task_completed)
    mark_button.pack(pady=5)

    # Erstellen der Schaltfläche zum Sortieren nach Aufgabentext
    sort_text_button = tk.Button(root, text="Nach Aufgabentext sortieren", command=sort_tasks_by_text)
    sort_text_button.pack(pady=5)
    
    # Erstellen der Schaltfläche zum Sortieren nach Erstellungsdatum
    sort_date_button = tk.Button(root, text="Nach Erstellungsdatum sortieren", command=sort_tasks_by_date)
    sort_date_button.pack(pady=5)

    # Erstellen der Schaltfläche zum Sortieren nach Fälligkeitsdatum
    

    # Erstellen der Schaltfläche zum Sortieren nach Priorität
    

    # Schließen der GUI und Speichern der Liste beim Beenden des Programms
    def exit_program():
        save_todo_list()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", exit_program)

    # Start der Hauptschleife der Benutzeroberfläche
    root.mainloop()

# Öffnen der Benutzeroberfläche, wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    todo_list = LinkedList()
    listbox = None
    entry = None
    priority_var = None
    date_var = None
    open_ui()
