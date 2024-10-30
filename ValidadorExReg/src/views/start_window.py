import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class StartWindow:
    """
    Ventana de inicio con una imagen y un botón para pasar a la ventana principal.

    Attributes:
        root (tk.Tk): La ventana raíz de Tkinter.
        main_window_class (class): La clase de la ventana principal que se abrirá.
        controller (object): El controlador que maneja la lógica de la aplicación.
        main_window_open (bool): Indicador de si la ventana principal ya está abierta.
    """

    def __init__(self, root, main_window_class, controller):
        """
        Inicializa la ventana de inicio.

        Args:
            root (tk.Tk): La ventana raíz de Tkinter.
            main_window_class (class): La clase de la ventana principal que se abrirá.
            controller (object): El controlador que maneja la lógica de la aplicación.
        """
        self.root = root
        self.main_window_class = main_window_class
        self.controller = controller
        self.main_window_open = False
        self._init_ui()

    def _init_ui(self):
        """
        Inicializa todos los componentes de la UI.
        """
        self.root.title("Inicio")
        self.root.geometry("1260x780")

        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Cargar y mostrar la imagen
        img_path = os.path.join(os.path.dirname(__file__), '../utils/PORT.png')
        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(main_frame, image=img)
        img_label.image = img  # Keep a reference to avoid garbage collection
        img_label.grid(row=0, column=0, padx=5, pady=5)

        # Botón para pasar a la ventana principal
        start_button = ttk.Button(
            main_frame,
            text="Iniciar",
            command=self._open_main_window
        )
        start_button.grid(row=1, column=0, pady=10)

    def _open_main_window(self):
        """
        Cierra la ventana de inicio y abre la ventana principal.
        """
        if not self.main_window_open:
            self.main_window_open = True
            self.root.destroy()
            main_window = self.main_window_class(self.controller)
            main_window.run()