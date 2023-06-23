import json
from TitelTaskListe import TitelTaskList
# Importiere die erforderlichen Module und Klassen

My_titel_list = TitelTaskList()  # Erzeuge eine Instanz für die Aufgabenliste mit Titeln
TitelListe = TitelTaskList()  # Erzeuge eine Instanz für die Titel der Aufgabenliste
Taskoftitellist = TitelTaskList()  # Erzeuge eine Instanz für die Aufgaben der Aufgabenliste
Ti_Li = TitelListe.get_tasks()  # Hole die Liste der Titel
Ti_Ta = Taskoftitellist.get_tasks()  # Hole die Liste der Aufgaben
counter = 1  # Initialisiere einen Zähler

while True:
    print("\n")
    print("1. Task Liste")
    print("2. Titel-Task-Liste")
    print("3. Beenden")
    choice = input("")  # Lese die Auswahl des Benutzers ein

    if choice == "1":  # Benutzer hat "1" gewählt (Task-Liste)
        print("\n")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgabe entfernen")
        print("3. Aufgaben anzeigen")
        print("4. Beenden")
        choice = input("Geben Sie Ihre Auswahl (1-4) ein: ")  # Lese die Auswahl des Benutzers ein

        if choice == "1":  # Benutzer hat "1" gewählt (Aufgabe hinzufügen)
            print("\n")
            task = input('Geben Sie Ihren To-Do-Punkt an: ')
            My_titel_list.add_task(task)  # Füge die Aufgabe zur Aufgabenliste hinzu
            with open('my_titel_list.json', 'w') as f:
                json.dump(My_titel_list.get_tasks(), f)  # Speichere die aktualisierte Aufgabenliste in einer JSON-Datei
        elif choice == "2":  # Benutzer hat "2" gewählt (Aufgabe entfernen)
            print("\n")
            task = input("Geben Sie den zu entfernenden To-Do-Punkt an: ")
            My_titel_list.remove_task(task)  # Entferne die Aufgabe aus der Aufgabenliste
            with open('my_titel_list.json', 'w') as f:
                json.dump(My_titel_list.get_tasks(), f)  # Speichere die aktualisierte Aufgabenliste in einer JSON-Datei

        elif choice == "3":  # Benutzer hat "3" gewählt (Aufgaben anzeigen)
            print("\n")
            print("\nAktualisierte To-Do-Liste:")
            with open('my_titel_list.json', "r") as f:
                json_data = json.load(f)  # Lade die Aufgabenliste aus der JSON-Datei

            liste = json_data  # Konvertiere die JSON-Daten in eine Liste

            print(liste)  # Gib die Liste der Aufgaben aus

        elif choice == "4":  # Benutzer hat "4" gewählt (Beenden)
            print("\n")
            print("Tschöö!")  # Beende das Programm
            break

        else:  # Benutzer hat eine ungültige Auswahl getroffen
            print("\n")
            print("Falsche Eingabe. Bitte 1, 2, 3 oder 4 eingeben.")

    elif choice == "2":  # Benutzer hat "2" gewählt (Titel-Task-Liste)
        print("\n")
        print("1. Titel mit To-Do/s hinzufügen")
        print("2. Titel mit To-Do/s entfernen")
        print("3. Titel und To-Dos anzeigen")
        print("4. Zurück")
        choice = input("Geben Sie Ihre Auswahl (1-4) ein: ")  # Lese die Auswahl des Benutzers ein

        if choice == "1":  # Benutzer hat "1" gewählt (Titel mit To-Do/s hinzufügen)
            print("\n")
            TitelListe.add_TitelTask(input("Welchen Titel sollen die To-Do/s haben?"), input("Welchen To_Do soll hinzugefügt werden?:"))
            with open('TitelListe.json', 'w') as f:
                json.dump(TitelListe.get_tasks(), f)  # Speichere die aktualisierte Titel-Task-Liste in einer JSON-Datei

        elif choice == "2":  # Benutzer hat "2" gewählt (Titel mit To-Do/s entfernen)
            print("\n")
            TitelListe.remove_TitelTask(input("Welcher Titel soll entfernt werden:"), input("Welche To-Do soll entfernt werden:"))
            with open('TitelListe.json', 'w') as f:
                json.dump(TitelListe.get_tasks(), f)  # Speichere die aktualisierte Titel-Task-Liste in einer JSON-Datei

        elif choice == "3":  # Benutzer hat "3" gewählt (Titel und To-Dos anzeigen)
            print("\n")
            with open('TitelListe.json', "r") as f:
                json_data = json.load(f)  # Lade die Titel-Task-Liste aus der JSON-Datei

            liste = json_data  # Konvertiere die JSON-Daten in eine Liste

            print(liste)  # Gib die Liste der Titel und To-Dos aus

        elif choice == "4":  # Benutzer hat "4" gewählt (Zurück)
            print("\n")
            print("Tschöö!")  # Beende das Programm
            break

        else:  # Benutzer hat eine ungültige Auswahl getroffen
            print("\n")
            print("Falsche Eingabe. Bitte 1, 2, 3 oder 4 eingeben.")

    elif choice == "3":  # Benutzer hat "3" gewählt (Beenden)
        break  # Beende das Programm

    else:  # Benutzer hat eine ungültige Auswahl getroffen
        print("\n")
        print("Falsche Eingabe. Bitte 1, 2 oder 3 eingeben.")
