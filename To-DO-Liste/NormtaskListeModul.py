# Definiere eine Klasse NormTaskList (normale Aufgabenliste)
class NormTaskList:
    def __init__(self):
        self.tasks = []  # Initialisiere eine leere Liste für Aufgaben
    
    def add_task(self, task):
        self.tasks.append(task)  # Füge eine Aufgabe zur Liste hinzu

    def remove_task(self, task):
        self.tasks.remove(task)  # Entferne eine Aufgabe aus der Liste

    def print_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")  # Gebe die Aufgaben mit ihrer Nummerierung aus