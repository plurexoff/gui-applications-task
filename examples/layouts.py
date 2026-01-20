"""
Пример 3: Расположение элементов (Layouts)
VBox, HBox, Grid, Form
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QPushButton
)
from PyQt5.QtGui import QFont


class LayoutsDemo(QMainWindow):
    """Layouts demonstration"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Initialize UI"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel('Layouts: VBox, HBox, Grid')
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        main_layout.addWidget(title)
        
        # Grid layout
        grid_layout = QGridLayout()
        
        labels = [
            ('(0,0)', 0, 0), ('(0,1)', 0, 1), ('(0,2)', 0, 2),
            ('(1,0)', 1, 0), ('(1,1)', 1, 1), ('(1,2)', 1, 2),
            ('(2,0)', 2, 0), ('(2,1)', 2, 1), ('(2,2)', 2, 2),
        ]
        
        for text, row, col in labels:
            label = QLabel(text)
            label.setStyleSheet("border: 1px solid black; padding: 10px; background-color: #e0e0e0;")
            grid_layout.addWidget(label, row, col)
        
        main_layout.addLayout(grid_layout)
        
        # HBox
        hbox_layout = QHBoxLayout()
        for i in range(3):
            btn = QPushButton(f'Кнопка {i+1}')
            hbox_layout.addWidget(btn)
        main_layout.addLayout(hbox_layout)
        
        central_widget.setLayout(main_layout)
        
        self.setWindowTitle('Layouts Demo')
        self.setGeometry(100, 100, 400, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LayoutsDemo()
    sys.exit(app.exec_())
