# Füllen Sie die Lücken entsprechend der Anleitung in README.md aus.

import  # Importiere das Zufallsmodul

def play_game():  # Definiere eine Funktion namens play_game
     # Druckt eine Willkommensnachricht
     # Druckt eine Nachricht über den Bereich der geheimen Zahl
     # Eine Meldung über die Anzahl der Versuche ausgeben

     # Erzeugen Sie eine Zufallszahl zwischen 1 und 100 und weisen Sie sie secret_number zu.
     # Initialisiere den Zähler der Versuche auf 0

    while  # Startet eine Schleife, die so lange läuft, wie attempts kleiner als 5 ist
          # Aufforderung an den Benutzer, einen Tipp einzugeben und diesen in eine ganze Zahl umzuwandeln
        versuche += 1 # Erhöht den Zähler der Versuche um 1

        if   # Überprüfen Sie, ob der Schätzwert kleiner als die geheime Zahl ist.
             # Eine Meldung ausgeben, dass der Wert zu niedrig ist
        elif  # Prüfen, ob der Schätzwert größer als die geheime Zahl ist
             # Eine Meldung ausgeben, die besagt, dass der Schätzwert zu hoch ist
        else:  # Wenn keine der obigen Bedingungen erfüllt ist, muss der Tipp richtig sein
             # Eine Meldung ausgeben, die besagt, dass der Tipp richtig ist
            return # Beenden Sie die Funktion
        
    if versuche == 5:
         # Wenn die Schleife beendet wird, ohne dass die richtige Zahl gefunden wurde, wird eine Meldung ausgegeben, dass die Versuche erschöpft sind
         # Druckt den Wert der geheimen Zahl

() # Rufen Sie die Funktion play_game auf, um das Spiel zu starten.
