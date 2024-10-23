import re
from typing import List, Tuple


class RegexModel:
    """Modelo para el manejo de expresiones regulares."""

    def __init__(self):
        self.current_regex: str = ""
        self.compiled_pattern = None

    def set_regex(self, regex: str) -> bool:
        """
        Establece y compila una nueva expresión regular.

        Args:
            regex (str): La expresión regular a compilar

        Returns:
            bool: True si la compilación fue exitosa, False en caso contrario
        """
        try:
            self.compiled_pattern = re.compile(regex)
            self.current_regex = regex
            return True
        except re.error:
            self.compiled_pattern = None
            return False

    def validate_strings(self, strings: List[str]) -> List[Tuple[str, bool]]:
        """
        Valida una lista de cadenas contra la expresión regular actual.

        Args:
            strings (List[str]): Lista de cadenas a validar

        Returns:
            List[Tuple[str, bool]]: Lista de tuplas (cadena, es_válida)
        """
        if not self.compiled_pattern:
            return [(s, False) for s in strings]

        return [(s, bool(self.compiled_pattern.fullmatch(s))) for s in strings]

    def explain_regex(self) -> str:
        """
        Genera una explicación en lenguaje natural de la expresión regular.

        Returns:
            str: Explicación de la expresión regular
        """
        if not self.current_regex:
            return "No hay expresión regular definida."

        # Aquí se implementará la lógica para explicar la regex
        # Por ahora retornamos un placeholder
        return f"Expresión regular: {self.current_regex}"