# Validador de Expresiones Regulares

## 📋 Descripción

Este proyecto implementa un validador de expresiones regulares con interfaz gráfica que permite a los usuarios verificar si determinadas cadenas de texto cumplen con los patrones definidos por una expresión regular. La herramienta está desarrollada en Python y proporciona una interfaz intuitiva para trabajar con expresiones regulares.

## ✨ Características Principales

- Interfaz gráfica amigable para el usuario
- Validación en tiempo real de expresiones regulares
- Soporte para múltiples cadenas de entrada
- Resaltado de sintaxis para expresiones regulares
- Manejo de errores y retroalimentación clara
- Explicaciones en lenguaje natural de las expresiones regulares
- Suite completa de pruebas unitarias

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/usuario/regex-validator.git
cd regex-validator
```

2. Crear y activar un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## 💻 Uso

1. Ejecutar la aplicación:

```bash
python src/main.py
```

2. En la interfaz:
   - Ingrese su expresión regular en el campo superior
   - Agregue las cadenas a validar en el área de texto
   - Presione el botón "Validar"
   - Observe los resultados en el área de salida

## 🛠️ Estructura del Proyecto

```
regex-validator/
├── src/
│   ├── main.py
│   ├── gui/
│   │   └── interface.py
│   ├── core/
│   │   ├── regex_parser.py
│   │   ├── validator.py
│   │   └── automata.py
│   └── utils/
│       └── error_handler.py
├── tests/
│   ├── test_parser.py
│   ├── test_validator.py
│   └── test_automata.py
├── docs/
│   ├── user_manual.md
│   └── technical_docs.md
├── requirements.txt
└── README.md
```

## 📚 Documentación

- [Manual de Usuario](docs/user_manual.md)
- [Documentación Técnica](docs/technical_docs.md)

## ⚙️ Tecnologías Utilizadas

- Python 3.8+
- Tkinter (interfaz gráfica)
- pytest (pruebas unitarias)
- regex (manejo de expresiones regulares)

## 🧪 Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest tests/
```

## 👥 Contribuidores

- Luis Ernesto Carballo Lopez.
- Jacobo Luengas Suaza.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📧 Contacto

Para cualquier pregunta o sugerencia, por favor abrir un issue en el repositorio.

## 🙏 Agradecimientos

- A nuestro profesor por la guía y apoyo durante el desarrollo
- A la comunidad de Python por las herramientas y bibliotecas utilizadas
