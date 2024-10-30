import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from src.controllers.regex_controller import RegexController
from src.utils.automata_generator import probar_automata
import os
import re

class MainWindow:
    """
    Ventana principal modernizada de Regexify.

    Attributes:
        controller (RegexController): El controlador que maneja la lógica de la aplicación.
        root (tk.Tk): La ventana raíz de Tkinter.
        colors (dict): Diccionario de colores para el tema oscuro moderno.
    """

    def __init__(self, controller: RegexController):
        """
        Inicializa la ventana principal.

        Args:
            controller (RegexController): El controlador que maneja la lógica de la aplicación.
        """
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Regexify")
        self.root.geometry("890x950")

        # Configurar tema oscuro moderno
        self.colors = {
            'bg': '#1E1E2E',            # Fondo principal
            'secondary': '#2A2A3F',     # Fondo secundario
            'accent': '#7F849C',        # Color de acento
            'text': '#CDD6F4',          # Color de texto principal
            'highlight': '#89B4FA',     # Color de resaltado
            'error': '#F38BA8',         # Color de error
            'success': '#A6E3A1'        # Color de exito
        }

        self.root.configure(bg=self.colors['bg'])
        self._init_styles()
        self._init_ui()

    def _init_styles(self):
        """
        Inicializa los estilos personalizados.
        """
        style = ttk.Style()
        style.theme_use('clam')

        # Estilo para frames
        style.configure(
            "Modern.TFrame",
            background=self.colors['bg']
        )

        # Estilo para LabelFrames
        style.configure(
            "Modern.TLabelframe",
            background=self.colors['bg'],
            foreground=self.colors['text']
        )
        style.configure(
            "Modern.TLabelframe.Label",
            background=self.colors['bg'],
            foreground=self.colors['text'],
            font=('Helvetica', 12, 'bold')
        )

        # Estilo para botones
        style.configure(
            "Modern.TButton",
            background=self.colors['accent'],
            foreground=self.colors['text'],
            padding=(20, 10),
            font=('Helvetica', 10),
            borderwidth=0
        )
        style.map(
            "Modern.TButton",
            background=[('active', self.colors['highlight'])]
        )

    def _create_modern_text(self, parent, height, **kwargs):
        """
        Crea un widget de texto con estilo moderno.

        Args:
            parent (tk.Widget): El widget padre.
            height (int): La altura del widget de texto.
            **kwargs: Argumentos adicionales para el widget de texto.

        Returns:
            tk.Text: El widget de texto creado.
        """
        text_widget = tk.Text(
            parent,
            height=height,
            bg=self.colors['secondary'],
            fg=self.colors['text'],
            insertbackground=self.colors['text'],
            selectbackground=self.colors['highlight'],
            selectforeground=self.colors['text'],
            font=('Consolas', 11),
            relief='flat',
            padx=10,
            pady=10,
            **kwargs
        )
        return text_widget

    def _init_ui(self):
        """
        Inicializa todos los componentes de la UI.
        """
        # Frame principal con padding
        main_frame = ttk.Frame(self.root, padding="20", style="Modern.TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Título de la aplicación
        title_label = tk.Label(
            main_frame,
            text="Regexify",
            font=('Helvetica', 24, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['highlight']
        )
        title_label.grid(row=0, column=0, pady=(0, 20))

        # Frame para la expresión regular
        regex_frame = ttk.LabelFrame(
            main_frame,
            text="Expresión Regular",
            padding="10",
            style="Modern.TLabelframe"
        )
        regex_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 20))

        self.regex_text = self._create_modern_text(regex_frame, height=2)
        self.regex_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.regex_text.bind("<KeyRelease>", self._highlight_syntax)

        # Frame para las cadenas de prueba
        test_frame = ttk.LabelFrame(
            main_frame,
            text="Cadenas de Prueba",
            padding="10",
            style="Modern.TLabelframe"
        )
        test_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 20))

        self.test_text = self._create_modern_text(test_frame, height=8)
        self.test_text.grid(row=0, column=0, sticky=(tk.W, tk.E))

        # Frame para los botones con diseño moderno
        buttons_frame = ttk.Frame(main_frame, style="Modern.TFrame")
        buttons_frame.grid(row=3, column=0, pady=(0, 20))

        # Contenedor para los botones con espaciado uniforme
        button_container = ttk.Frame(buttons_frame, style="Modern.TFrame")
        button_container.grid(row=0, column=0)

        # Botones con iconos (usando caracteres Unicode como ejemplo)
        buttons = [
            ("Validar ✓", self._validate),
            ("Generar Autómata ⚙", self._generate_automata),
            ("Explicar", self._explain_regex),
            ("Limpiar", self._clear_results)  # Added "Limpiar" button
        ]

        for idx, (text, command) in enumerate(buttons):
            btn = ttk.Button(
                button_container,
                text=text,
                command=command,
                style="Modern.TButton"
            )
            btn.grid(row=0, column=idx, padx=10)

        # Frame para resultados
        results_frame = ttk.LabelFrame(
            main_frame,
            text="Resultados",
            padding="10",
            style="Modern.TLabelframe"
        )
        results_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(0, 20))

        self.results_text = self._create_modern_text(results_frame, height=8, state='disabled')
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E))

        # Cargar y mostrar el icono con estilo moderno
        icon_path = os.path.join(os.path.dirname(__file__), '../utils/expresiones.png')
        if os.path.exists(icon_path):
            icon_image = Image.open(icon_path)
            icon_image = icon_image.resize((60, 60), Image.ANTIALIAS)
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label = tk.Label(
                main_frame,
                image=icon_photo,
                bg=self.colors['bg'],
                relief='flat'
            )
            icon_label.image = icon_photo
            icon_label.grid(row=5, column=0, pady=20)

        # Configurar tags para el resaltado de sintaxis
        self.regex_text.tag_configure("block1", foreground=self.colors['success'])
        self.regex_text.tag_configure("block2", foreground=self.colors['highlight'])
        self.regex_text.tag_configure("block3", foreground=self.colors['error'])

    def _highlight_syntax(self, event=None):
        """
        Resalta la sintaxis de la expresión regular.

        Args:
            event (tk.Event, optional): El evento de teclado que dispara el resaltado de sintaxis.
        """
        regex = self.regex_text.get("1.0", tk.END).strip()
        self.regex_text.tag_remove("block1", "1.0", tk.END)
        self.regex_text.tag_remove("block2", "1.0", tk.END)
        self.regex_text.tag_remove("block3", "1.0", tk.END)

        patterns = [
            (r"[a-zA-Z0-9]+", "block1"),
            (r"[.*+?^${}()|[\]\\]+", "block2"),
            (r"[\(\)]+", "block3")
        ]

        for pattern, tag in patterns:
            for match in re.finditer(pattern, regex):
                start, end = match.span()
                self.regex_text.tag_add(tag, f"1.{start}", f"1.{end}")

    def _validate(self):
        """
        Maneja el evento de validación.
        """
        regex = self.regex_text.get("1.0", tk.END).strip()
        if not self.controller.set_regex_pattern(regex):
            messagebox.showerror(
                "Error",
                "La expresión regular no es válida"
            )
            return

        test_strings = self.test_text.get("1.0", tk.END).split('\n')
        results = self.controller.validate_strings(test_strings)

        self.results_text.configure(state='normal')
        self.results_text.delete("1.0", tk.END)

        for string, is_valid in results:
            result = "✓" if is_valid else "✗"
            color_tag = "success" if is_valid else "error"
            self.results_text.insert(tk.END, f"{string}: ")
            self.results_text.insert(tk.END, f"{result}\n", color_tag)

        self.results_text.tag_configure("success", foreground=self.colors['success'])
        self.results_text.tag_configure("error", foreground=self.colors['error'])
        self.results_text.configure(state='disabled')

    def _generate_automata(self):
        """
        Maneja el evento de generación de autómata.
        """
        regex = self.regex_text.get("1.0", tk.END).strip()
        probar_automata(regex)

        # Mostrar la imagen generada en una ventana moderna
        img = Image.open('automata.png')
        img_window = tk.Toplevel(self.root)
        img_window.title("Autómata Generado")
        img_window.configure(bg=self.colors['bg'])

        # Ajustar el tamaño de la imagen manteniendo la proporción
        max_size = (700, 500)
        img.thumbnail(max_size, Image.ANTIALIAS)
        img_photo = ImageTk.PhotoImage(img)

        img_frame = ttk.Frame(img_window, style="Modern.TFrame", padding=20)
        img_frame.pack(fill=tk.BOTH, expand=True)

        img_label = tk.Label(
            img_frame,
            image=img_photo,
            bg=self.colors['bg'],
            relief='flat'
        )
        img_label.image = img_photo
        img_label.pack()

    def _explain_regex(self):
        """
        Muestra la explicación de la expresión regular.
        """
        explanation = self.controller.get_regex_explanation()

        # Crear una ventana moderna para la explicación
        explain_window = tk.Toplevel(self.root)
        explain_window.title("Explicación de la Expresión Regular")
        explain_window.configure(bg=self.colors['bg'])
        explain_window.geometry("600x400")

        explain_frame = ttk.Frame(
            explain_window,
            style="Modern.TFrame",
            padding=20
        )
        explain_frame.pack(fill=tk.BOTH, expand=True)

        explain_text = self._create_modern_text(
            explain_frame,
            height=15,
            wrap=tk.WORD
        )
        explain_text.insert("1.0", explanation)
        explain_text.configure(state='disabled')
        explain_text.pack(fill=tk.BOTH, expand=True)

    def _clear_results(self):
        """
        Limpia el panel de resultados y las explicaciones almacenadas.
        """
        self.results_text.configure(state='normal')
        self.results_text.delete("1.0", tk.END)
        self.results_text.configure(state='disabled')
        self.controller.clear_patterns()

    def run(self):
        """
        Inicia la aplicación.
        """
        # Centrar la ventana en la pantalla
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        self.root.mainloop()