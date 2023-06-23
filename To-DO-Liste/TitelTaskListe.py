
from NormtaskListeModul import NormTaskList
# Definiere eine abgeleitete Klasse TitelTaskList (Aufgabenliste mit Titeln)
class TitelTaskList(NormTaskList):
    
    def get_tasks(self):
        return self.tasks  # Gibt die Liste der Aufgaben zurück
    
    def add_TitelTask(self, Titel, Task):
        TitelTask= (Titel,Task)
        self.tasks.append(TitelTask)  # Füge eine Aufgabe zur Liste hinzu
   
    def remove_TitelTask(self, Titel, Task):
        TitelTask = (Titel, Task)
        self.tasks.remove(TitelTask)