from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog
import sys

from converter import text_to_hex, hex_to_text
from validator import is_valid_hex
from file_manager import read_text_file, save_text_file

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hex Editor")
window.resize(600, 400)

layout = QVBoxLayout()

text_input = QTextEdit()
text_input.setPlaceholderText("Entrez du texte ici...")

hex_output = QTextEdit()
hex_output.setPlaceholderText("Résultat en hex...")

layout.addWidget(text_input)
layout.addWidget(hex_output)

""" BTN txt to hex """
convert_button = QPushButton("Texte -> Hex")
layout.addWidget(convert_button)

def convert_text():
    text = text_input.toPlainText()
    result = text_to_hex(text)
    hex_output.setPlainText(result)
convert_button.clicked.connect(convert_text)

""" BTN hex to txt """
hex_to_text_button = QPushButton("Hex -> Texte")
layout.addWidget(hex_to_text_button)

def convert_hex():
    hex_text = hex_output.toPlainText()

    if not is_valid_hex(hex_text):
        hex_output.setPlainText("Hex invalide")
        return

    result = hex_to_text(hex_text)
    text_input.setPlainText(result)
hex_to_text_button.clicked.connect(convert_hex)

""" BTN open file """
open_button = QPushButton("Ouvrir fichier")
layout.addWidget(open_button)

def open_file():
    file_path, _ = QFileDialog.getOpenFileName(window, "Ouvrir un fichier", "", "Text Files (*.txt)")

    if file_path:
        content = read_text_file(file_path)
        if content:
            text_input.setPlainText(content)
open_button.clicked.connect(open_file)

""" BTN save file """
save_button = QPushButton("Enregistrer")
layout.addWidget(save_button)

def save_file():
    file_path, _ = QFileDialog.getSaveFileName(window, "Enregistrer le fichier", "", "Text Files (*.txt)")

    if file_path:
        content = text_input.toPlainText()
        save_text_file(file_path, content)
save_button.clicked.connect(save_file)


window.setLayout(layout)
window.show()
sys.exit(app.exec())