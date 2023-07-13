# Ergänze den Code an den entsprechenden Stellen nach der README.md Anleitung.

import tkinter as tk
import pickle
import os
import datetime

# Code für die Implementierung der verketteten Liste hier einfügen
class Node:
    

class LinkedList:
    

    def append(self, data):
        
        if self.head is None:
            
        else:
            

    def remove(self, index):
        

    def __iter__(self):
        

# Laden der To-Do-Liste
def load_todo_list():
    

# Speichern der To-Do-Liste
def save_todo_list():
    

# Funktion zum Hinzufügen einer Aufgabe
def add_task():
    
        
# Funktion zum Sortieren der Aufgaben nach Aufgabentext
def sort_tasks_by_text():
    

# Funktion zum Sortieren der Aufgaben nach Erstellungsdatum
def sort_tasks_by_date():
    

# Funktion zum Aktualisieren der Listbox
def refresh_listbox():
    
        
# Markieren einer Aufgabe als erledigt
def mark_task_completed():
    

# Öffnen der Benutzeroberfläche
def open_ui():
    global todo_list, listbox, entry
    root = tk.Tk()
    root.title("To-Do-Liste")

    # Laden der To-Do-Liste
    todo_list = load_todo_list()

    # Erstellen der Listbox
    listbox = tk.Listbox(root, width=50)
    listbox.pack(pady=10)

    # Hinzufügen der vorhandenen Aufgaben zur Listbox
    for task in todo_list:
        listbox.insert(tk.END, task[0])

    # Erstellen des Eingabefelds und der Schaltfläche zum Hinzufügen von Aufgaben
    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)
    add_button = tk.Button(root, text="Aufgabe hinzufügen", command=add_task)
    add_button.pack(pady=5)

    # Erstellen der Schaltfläche zum Markieren einer Aufgabe als erledigt
    mark_button = tk.Button(root, text="Aufgabe erledigt", command=mark_task_completed)
    mark_button.pack(pady=5)
    
    # Erstellen der Schaltfläche zum Sortieren nach Aufgabentext
    

    # Erstellen der Schaltfläche zum Sortieren nach Erstellungsdatum
    

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
    open_ui()
