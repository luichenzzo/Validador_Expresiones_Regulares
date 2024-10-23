from typing import List
from src.models.regex_model import RegexModel


class RegexController:
    """Controlador principal para la aplicación de validación de regex."""

    def __init__(self, model: RegexModel):
        self.model = model

    def set_regex_pattern(self, pattern: str) -> bool:
        """
        Establece un nuevo patrón de expresión regular.

        Args:
            pattern (str): El patrón de expresión regular

        Returns:
            bool: True si el patrón es válido, False en caso contrario
        """
        return self.model.set_regex(pattern)

    def validate_strings(self, strings: List[str]) -> List[tuple]:
        """
        Valida una lista de cadenas contra el patrón actual.

        Args:
            strings (List[str]): Lista de cadenas a validar

        Returns:
            List[tuple]: Lista de resultados (cadena, es_válida)
        """
        # Limpiamos las cadenas de entrada
        cleaned_strings = [s.strip() for s in strings if s.strip()]
        return self.model.validate_strings(cleaned_strings)

    def get_regex_explanation(self) -> str:
        """
        Obtiene la explicación de la expresión regular actual.

        Returns:
            str: Explicación en lenguaje natural
        """
        return self.model.explain_regex()