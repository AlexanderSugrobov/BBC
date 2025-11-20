import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
)

class TextAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анализ текста")
        self.setFixedSize(400, 400)
        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.btn_analyze = QPushButton("Анализ:")
        self.btn_analyze.clicked.connect(self.analyze_text)
        layout.addWidget(self.btn_analyze)


        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def analyze_text(self):
        text = self.text_edit.toPlainText()

        total_chars = len(text)
        spaces = text.count(" ")
        chars_no_spaces = len(text.replace(" ", ""))

        result = (
            f"Всего символов: {total_chars}\n"
            f"Пробелов: {spaces}\n"
            f"Символов без пробелов: {chars_no_spaces}"
        )

        self.result_label.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextAnalyzer()
    window.show()
    sys.exit(app.exec())
