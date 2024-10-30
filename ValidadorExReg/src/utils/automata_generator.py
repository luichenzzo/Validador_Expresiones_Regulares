import os
from graphviz import Digraph
from PIL import Image

# Add Graphviz bin directory to PATH
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

class Estado:
    """
    Representa un estado en el autómata.

    Attributes:
        id (str): Identificador del estado.
        transiciones (dict): Diccionario de transiciones del estado.
        es_final (bool): Indica si el estado es final.
    """
    def __init__(self, id):
        """
        Inicializa un estado con un identificador.

        Args:
            id (str): Identificador del estado.
        """
        self.id = id
        self.transiciones = {}
        self.es_final = False

class Automata:
    """
    Representa un autómata finito.

    Attributes:
        estados (dict): Diccionario de estados del autómata.
        estado_inicial (str): Identificador del estado inicial.
        contador_estados (int): Contador de estados creados.
    """
    def __init__(self):
        """
        Inicializa un autómata vacío.
        """
        self.estados = {}
        self.estado_inicial = None
        self.contador_estados = 0

    def crear_estado(self):
        """
        Crea un nuevo estado en el autómata.

        Returns:
            str: Identificador del nuevo estado.
        """
        id_estado = f'q{self.contador_estados}'
        self.contador_estados += 1
        self.estados[id_estado] = Estado(id_estado)
        return id_estado

    def agregar_transicion(self, estado_origen, simbolo, estado_destino):
        """
        Agrega una transición entre dos estados.

        Args:
            estado_origen (str): Identificador del estado de origen.
            simbolo (str): Símbolo de la transición.
            estado_destino (str): Identificador del estado de destino.
        """
        if simbolo not in self.estados[estado_origen].transiciones:
            self.estados[estado_origen].transiciones[simbolo] = set()
        self.estados[estado_origen].transiciones[simbolo].add(estado_destino)

class GeneradorAutomata:
    """
    Generador de autómatas a partir de expresiones regulares.

    Attributes:
        automata (Automata): El autómata generado.
    """
    def __init__(self):
        """
        Inicializa el generador de autómatas.
        """
        self.automata = None

    def procesar_expresion(self, expr):
        """
        Procesa una expresión regular y genera un autómata.

        Args:
            expr (str): La expresión regular a procesar.

        Returns:
            Automata: El autómata generado.
        """
        self.automata = Automata()

        # Crear estado inicial
        estado_inicial = self.automata.crear_estado()
        self.automata.estado_inicial = estado_inicial

        # Procesar la expresión
        estado_actual = estado_inicial
        estado_actual = self.procesar_subexpresion(estado_actual, expr)

        # Marcar el estado final
        self.automata.estados[estado_actual].es_final = True
        return self.automata

    def procesar_subexpresion(self, estado_inicial, subexpr):
        """
        Procesa una subexpresión de la expresión regular.

        Args:
            estado_inicial (str): Identificador del estado inicial.
            subexpr (str): La subexpresión a procesar.

        Returns:
            str: Identificador del estado actual después de procesar la subexpresión.
        """
        estado_actual = estado_inicial
        i = 0
        while i < len(subexpr):
            if subexpr[i] == '|':
                # Manejar la unión (OR) creando caminos alternativos desde el mismo nodo inicial
                estado_actual = self.procesar_union(estado_inicial, subexpr)
                break
            elif subexpr[i] == '(':
                # Encontrar el paréntesis de cierre correspondiente
                nivel = 1
                j = i + 1
                while j < len(subexpr) and nivel > 0:
                    if subexpr[j] == '(':
                        nivel += 1
                    elif subexpr[j] == ')':
                        nivel -= 1
                    j += 1

                # Procesar la subexpresión dentro de los paréntesis
                subexpr_interna = subexpr[i + 1:j - 1]
                estado_actual = self.procesar_subexpresion(estado_actual, subexpr_interna)
                i = j
            elif subexpr[i] in '*+':
                # Manejar la clausura de Kleene y el operador +
                estado_actual = self.procesar_estrella(estado_actual, subexpr, i)
                i += 1
            else:
                # Manejar símbolos literales
                nuevo_estado = self.automata.crear_estado()
                self.automata.agregar_transicion(estado_actual, subexpr[i], nuevo_estado)
                estado_actual = nuevo_estado
                i += 1
        return estado_actual

    def procesar_estrella(self, estado_inicial, expr, i):
        """
        Procesa el operador de clausura de Kleene y el operador +.

        Args:
            estado_inicial (str): Identificador del estado inicial.
            expr (str): La expresión regular.
            i (int): Índice del operador en la expresión.

        Returns:
            str: Identificador del estado actual después de procesar el operador.
        """
        if expr[i - 1] == ')':
            # Encontrar el paréntesis de apertura correspondiente
            nivel = 1
            j = i - 2
            while j >= 0 and nivel > 0:
                if expr[j] == ')':
                    nivel += 1
                elif expr[j] == '(':
                    nivel -= 1
                j -= 1

            subexpr = expr[j + 2:i - 1]
            estado_intermedio = self.procesar_subexpresion(estado_inicial, subexpr)
            self.automata.agregar_transicion(estado_intermedio, '', estado_inicial)
            return estado_intermedio
        else:
            simbolo = expr[i - 1]
            self.automata.agregar_transicion(estado_inicial, simbolo, estado_inicial)
            return estado_inicial

    def procesar_union(self, estado_inicial, expr):
        """
        Procesa el operador de unión (OR).

        Args:
            estado_inicial (str): Identificador del estado inicial.
            expr (str): La expresión regular.

        Returns:
            str: Identificador del estado final después de procesar la unión.
        """
        estado_final = self.automata.crear_estado()
        partes = expr.split('|')
        for parte in partes:
            estado_actual = estado_inicial
            for simbolo in parte:
                nuevo_estado = self.automata.crear_estado() if simbolo != parte[-1] else estado_final
                self.automata.agregar_transicion(estado_actual, simbolo, nuevo_estado)
                estado_actual = nuevo_estado
        return estado_final

    def visualizar_automata(self):
        """
        Genera una visualización del autómata usando Graphviz.

        Returns:
            Digraph: El objeto Digraph de Graphviz que representa el autómata.
        """
        dot = Digraph(comment='Autómata Finito')
        dot.attr(rankdir='LR')

        for estado_id, estado in self.automata.estados.items():
            if estado.es_final:
                dot.node(estado_id, estado_id, shape='doublecircle')
            else:
                dot.node(estado_id, estado_id, shape='circle')

        dot.node('', '', shape='none')
        dot.edge('', self.automata.estado_inicial)

        for estado_id, estado in self.automata.estados.items():
            for simbolo, destinos in estado.transiciones.items():
                for destino in destinos:
                    dot.edge(estado_id, destino, label=simbolo)

        return dot

def probar_automata(expr):
    """
    Genera y visualiza un autómata a partir de una expresión regular.

    Args:
        expr (str): La expresión regular a procesar.
    """
    generador = GeneradorAutomata()
    automata = generador.procesar_expresion(expr)
    dot = generador.visualizar_automata()

    dot.render('automata', format='png', cleanup=True)
    print(f"Autómata generado para la expresión: {expr}")
    print("El autómata ha sido guardado como 'automata.png'")

    img = Image.open('automata.png')
    img.show()