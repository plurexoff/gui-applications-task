"""
Пример 4: Настройка стилей (Styling)
QSS - это Qt Style Sheets
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel
)
from PyQt5.QtGui import QFont


class StylingDemo(QMainWindow):
    """Styling demonstration"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Initialize UI"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel('Настройка стилей')
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Button 1
        btn1 = QPushButton('Кнопка Нормальная')
        btn1.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        layout.addWidget(btn1)
        
        # Button 2
        btn2 = QPushButton('Кнопка Опасная')
        btn2.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        layout.addWidget(btn2)
        
        # Button 3
        btn3 = QPushButton('Кнопка Инфо')
        btn3.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        layout.addWidget(btn3)
        
        central_widget.setLayout(layout)
        
        self.setWindowTitle('Styling Demo')
        self.setGeometry(100, 100, 300, 300)
        self.setStyleSheet("QMainWindow { background-color: #f5f5f5; }")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StylingDemo()
    sys.exit(app.exec_())
