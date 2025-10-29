import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel
from sdkFP.Guardar import Guardar
from sdkFP.Consultar import Consultar
"""
class Guardar:
    def agregar(self, titulo, autor):
        return f"Libro '{titulo}' de {autor} agregado (simulado)."

class Consultar:
    def consultar_libros(self):
        return ["Libro 1\n", "Libro 2\n"]

# El resto del código igual
"""

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Libros")
        self.setGeometry(100, 100, 400, 400)

        self.guardar = Guardar()
        self.consultar = Consultar()

        layout = QVBoxLayout()

        self.titulo = QLineEdit()
        self.autor = QLineEdit()
        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)

        layout.addWidget(QLabel("Título"))
        layout.addWidget(self.titulo)
        layout.addWidget(QLabel("Autor"))
        layout.addWidget(self.autor)

        boton_agregar = QPushButton("Agregar libro")
        boton_agregar.clicked.connect(self.accion_agregar_libro)

        boton_consultar = QPushButton("Consultar libros")
        boton_consultar.clicked.connect(self.accion_consultar_libros)

        layout.addWidget(boton_agregar)
        layout.addWidget(boton_consultar)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def accion_agregar_libro(self):
        titulo = self.titulo.text()
        autor = self.autor.text()
        mensaje = self.guardar.agregar(titulo, autor)
        self.resultado.setText(mensaje)

    def accion_consultar_libros(self):
        libros = self.consultar.consultar_libros()
        if libros:
            self.resultado.setText("".join(libros))
        else:
            self.resultado.setText("No hay libros registrados.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = App()
    ventana.show()
    sys.exit(app.exec())
