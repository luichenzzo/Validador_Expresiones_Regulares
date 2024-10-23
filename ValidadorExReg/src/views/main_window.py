import tkinter as tk
from tkinter import ttk, messagebox
from src.controllers.regex_controller import RegexController


class MainWindow:
    """Ventana principal de la aplicación."""

    def __init__(self, controller: RegexController):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Validador de Expresiones Regulares")
        self.root.geometry("800x600")

        self._init_ui()

    def _init_ui(self):
        """Inicializa todos los componentes de la UI."""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Frame para la expresión regular
        regex_frame = ttk.LabelFrame(main_frame, text="Expresión Regular", padding="5")
        regex_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

        self.regex_var = tk.StringVar()
        self.regex_entry = ttk.Entry(regex_frame, textvariable=self.regex_var, width=50)
        self.regex_entry.grid(row=0, column=0, padx=5, pady=5)

        # Frame para las cadenas de prueba
        test_frame = ttk.LabelFrame(main_frame, text="Cadenas de Prueba", padding="5")
        test_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.test_text = tk.Text(test_frame, height=10, width=50)
        self.test_text.grid(row=0, column=0, padx=5, pady=5)

        # Botón de validación
        self.validate_button = ttk.Button(
            main_frame,
            text="Validar",
            command=self._validate
        )
        self.validate_button.grid(row=2, column=0, pady=10)

        # Frame para resultados
        results_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="5")
        results_frame.grid(row=3, column=0, sticky=(tk.W, tk.E))

        self.results_text = tk.Text(results_frame, height=10, width=50, state='disabled')
        self.results_text.grid(row=0, column=0, padx=5, pady=5)

    def _validate(self):
        """Maneja el evento de validación."""
        regex = self.regex_var.get()
        if not self.controller.set_regex_pattern(regex):
            messagebox.showerror(
                "Error",
                "La expresión regular no es válida"
            )
            return

        # Obtener las cadenas de prueba
        test_strings = self.test_text.get("1.0", tk.END).split('\n')
        results = self.controller.validate_strings(test_strings)

        # Mostrar resultados
        self.results_text.configure(state='normal')
        self.results_text.delete("1.0", tk.END)

        for string, is_valid in results:
            result = "✓" if is_valid else "✗"
            self.results_text.insert(
                tk.END,
                f"{string}: {result}\n"
            )

        self.results_text.configure(state='disabled')

    def run(self):
        """Inicia la aplicación."""
        self.root.mainloop()