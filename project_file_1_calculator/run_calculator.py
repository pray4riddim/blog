import sys
import Core
from PyQt6.QtGui import QPalette, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QSizePolicy,
)
from PyQt6.QtGui import QIcon


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("计算器")

        # 添加一个主窗口部件
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # 创建垂直布局
        layout = QVBoxLayout()

        # 设置窗口的样式
        style_sheet = "background-image: url('background_image.jpg');"  # 替换为实际的背景图片路径
        self.setStyleSheet(style_sheet)

        # 创建显示结果的文本框
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        # 创建一个水平布局用于放置输入框和按钮
        input_layout = QHBoxLayout()
        layout.addLayout(input_layout)

        # 创建标签和输入框
        input_label = QLabel("输入表达式：")
        self.input_field = QLineEdit()
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_field)

        # 创建一个网格布局用于放置操作按钮
        button_grid = QGridLayout()
        layout.addLayout(button_grid)

        # 创建按钮并添加到网格布局中
        clear_button = QPushButton("清除")
        clear_button.clicked.connect(self.clear_input)
        button_grid.addWidget(clear_button, 0, 0, 1, 2)

        backspace_button = QPushButton()
        backspace_button.setIcon(QIcon("backspace_icon.png"))  # 设置退回按钮的图标
        backspace_button.clicked.connect(self.backspace)
        button_grid.addWidget(backspace_button, 0, 2)

        equal_button = QPushButton("=")
        equal_button.clicked.connect(self.calculate_expression)
        button_grid.addWidget(equal_button, 0, 3)

        button_labels = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("+", 4, 2),
        ]

        for label, row, col in button_labels:
            button = QPushButton(label)
            button.clicked.connect(lambda checked, text=label: self.add_to_input(text))
            button_grid.addWidget(button, row, col)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # 将布局设置为主窗口部件的布局
        main_widget.setLayout(layout)

    def clear_input(self):
        self.input_field.clear()
        self.result_display.clear()

    def add_to_input(self, text):
        current_text = self.input_field.text()
        self.input_field.setText(current_text + text)

    def backspace(self):
        current_text = self.input_field.text()
        self.input_field.setText(current_text[:-1])

    def calculate_expression(self):  # 计算表达式
        expression = self.input_field.text()
        try:
            result = str(Core.calculate(expression))
            self.result_display.setText(result)
        except Exception:
            self.result_display.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())
