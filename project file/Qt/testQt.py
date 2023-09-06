import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setMinimumSize(300, 400)

        # 创建显示结果的文本框
        self.result_label = QLabel()
        self.result_label.setStyleSheet("font-size: 20px; padding: 10px;")
        self.result_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.result_label.setFixedHeight(60)

        # 创建数字和运算符按钮
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "=", "+",
            "C"  # 归零按钮
        ]
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)
        positions = [(i, j) for i in range(5) for j in range(4)]
        
        self.equation = ""
        
        for position, button_text in zip(positions, buttons):
            button = QPushButton(button_text)
            button.setFixedSize(60, 60)
            button.clicked.connect(lambda state, text=button_text: self.button_clicked(text))
            grid_layout.addWidget(button, *position)

        # 创建主窗口的布局
        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        layout.addLayout(grid_layout)

        # 创建一个主 widget 并将布局设置给它
        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)

    def button_clicked(self, text):
        if text == "=":
            self.result_label.setText(str(eval(self.equation)))  # 计算结果并显示
        elif text == "C":
            self.equation = ""  # 归零操作
            self.result_label.setText("")  # 清空显示
        else:
            self.equation += text  # 将按钮的文本添加到等式中
            self.result_label.setText(self.equation)  # 更新显示

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CalculatorWindow()
    window.show()

    sys.exit(app.exec())