from src.models.regex_model import RegexModel
from src.controllers.regex_controller import RegexController
from src.views.main_window import MainWindow


def main():
    # Crear instancias de los componentes MVC
    model = RegexModel()
    controller = RegexController(model)
    view = MainWindow(controller)

    # Iniciar la aplicación
    view.run()


if __name__ == "__main__":
    main()