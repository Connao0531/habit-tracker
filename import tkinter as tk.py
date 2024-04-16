import tkinter as tk
from tkinter import messagebox
import json
import os

class HabitTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Habit Tracker")

        # Diccionario para almacenar los datos de los hábitos
        self.habits_data = {
            "Monday": {"Dormir": "", "Ejercicio": "", "Leer": ""},
            "Tuesday": {"Dormir": "", "Ejercicio": "", "Leer": ""},
            "Wednesday": {"Dormir": "", "Ejercicio": "", "Leer": ""},
            "Thursday": {"Dormir": "", "Ejercicio": "", "Leer": ""},
            "Friday": {"Dormir": "", "Ejercicio": "", "Leer": ""},
            "Saturday": {"Dormir": "", "Ejercicio": "", "Leer": ""},
            "Sunday": {"Dormir": "", "Ejercicio": "", "Leer": ""}
        }

        # Etiqueta y menú desplegable para seleccionar el día de la semana
        self.day_label = tk.Label(master, text="¿Qué día es hoy?")
        self.day_label.pack()
        self.day_var = tk.StringVar(master)
        self.day_var.set("Monday")  # Valor predeterminado
        self.day_menu = tk.OptionMenu(master, self.day_var, *self.habits_data.keys())
        self.day_menu.pack()

        # Botón para comenzar a ingresar los hábitos
        self.start_button = tk.Button(master, text="Comenzar", command=self.start_input)
        self.start_button.pack()

    def start_input(self):
        # Función para comenzar a ingresar los hábitos para el día seleccionado
        selected_day = self.day_var.get()
        habits = ["Dormir", "Ejercicio", "Leer"]
        for habit in habits:
            # Se pregunta por cada hábito y se almacena la respuesta en el diccionario
            answer = messagebox.askquestion("Habit Tracker", f"¿Lograste {habit} hoy?")
            if answer == "yes":
                self.habits_data[selected_day][habit] = "Logrado"
            else:
                self.habits_data[selected_day][habit] = "No logrado"
        # Guardar los datos en un archivo JSON
        with open("habits_data.json", "w") as file:
            json.dump(self.habits_data, file)
        messagebox.showinfo("Habit Tracker", "Datos guardados exitosamente.")
        # Abrir el archivo JSON para verificar los datos guardados
        self.open_json_file()

    def open_json_file(self):
        # Función para abrir el archivo JSON en el visor de texto predeterminado
        file_path = os.path.abspath("habits_data.json")
        try:
            os.system(f"start {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo JSON: {str(e)}")

def main():
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
