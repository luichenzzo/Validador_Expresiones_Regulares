from src.models.regex_model import RegexModel
from src.controllers.regex_controller import RegexController
from src.views.main_window import MainWindow
from src.views.start_window import StartWindow
import tkinter as tk

def main():
    # Crear instancias de los componentes MVC
    model = RegexModel()
    controller = RegexController(model)

    # Iniciar la ventana de inicio
    root = tk.Tk()
    start_window = StartWindow(root, MainWindow, controller)
    root.mainloop()

if __name__ == "__main__":
    main()