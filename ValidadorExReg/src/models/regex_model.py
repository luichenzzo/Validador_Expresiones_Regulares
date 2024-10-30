import re
from typing import List

class RegexModel:
    """Modelo para manejar la lógica de las expresiones regulares."""

    def __init__(self):
        self.patterns = []

    def set_regex(self, pattern: str) -> bool:
        """
        Establece un nuevo patrón de expresión regular.

        Args:
            pattern (str): El patrón de expresión regular

        Returns:
            bool: True si el patrón es válido, False en caso contrario
        """
        try:
            re.compile(pattern)
            self.patterns.append(pattern)
            return True
        except re.error:
            return False

    def validate_strings(self, strings: List[str]) -> List[tuple]:
        """
        Valida una lista de cadenas contra el patrón actual.

        Args:
            strings (List[str]): Lista de cadenas a validar

        Returns:
            List[tuple]: Lista de resultados (cadena, es_válida)
        """
        if not self.patterns:
            return [(s, False) for s in strings]

        results = []
        for pattern in self.patterns:
            regex = re.compile(pattern)
            results.extend([(s, bool(regex.match(s))) for s in strings])
        return results

    def explain_regex(self) -> str:
        """
        Explica las expresiones regulares actuales en lenguaje natural.

        Returns:
            str: Explicación en lenguaje natural
        """
        if not self.patterns:
            return "No hay patrones de expresión regular establecidos."

        explanations = {
            '.': 'cualquier carácter excepto una nueva línea',
            '*': 'cero o más repeticiones del carácter anterior',
            '+': 'una o más repeticiones del carácter anterior',
            '?': 'cero o una repetición del carácter anterior',
            '^': 'inicio de la cadena',
            '$': 'fin de la cadena',
            '\\d': 'cualquier dígito',
            '\\D': 'cualquier carácter que no sea un dígito',
            '\\w': 'cualquier carácter de palabra (letra, dígito o guion bajo)',
            '\\W': 'cualquier carácter que no sea de palabra',
            '\\s': 'cualquier espacio en blanco',
            '\\S': 'cualquier carácter que no sea un espacio en blanco',
            '[abc]': 'cualquier carácter a, b o c',
            '[^abc]': 'cualquier carácter excepto a, b o c',
            '(...)': 'grupo de captura',
            '(?:...)': 'grupo sin captura',
            '\\b': 'límite de palabra',
            '\\B': 'no límite de palabra'
        }

        explanation = []
        for pattern in self.patterns:
            explanation.append(f"Patrón: {pattern}")
            for char in pattern:
                if char in explanations:
                    explanation.append(explanations[char])
                else:
                    explanation.append(f"'{char}'")
            explanation.append("\n")

        return ' '.join(explanation)

    def clear_patterns(self):
        """Limpia todos los patrones de expresión regular almacenados."""
        self.patterns = []