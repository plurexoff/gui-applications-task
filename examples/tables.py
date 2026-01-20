"""
Пример 6: Таблицы
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QLabel
)
from PyQt5.QtGui import QFont


class TablesDemo(QMainWindow):
    """Tables demonstration"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Initialize UI"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        title = QLabel('Таблица план аних')
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Create table
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Название', 'Возраст', 'Отдел'])
        
        # Fill data
        data = [
            ['Иван', '25', 'IT'],
            ['Мария', '30', 'HR'],
            ['Петр', '28', 'IT'],
            ['Анна', '26', 'Finance'],
            ['Олег', '32', 'IT'],
        ]
        
        for row, row_data in enumerate(data):
            for col, item_text in enumerate(row_data):
                item = QTableWidgetItem(item_text)
                self.table.setItem(row, col, item)
        
        layout.addWidget(self.table)
        central_widget.setLayout(layout)
        
        self.setWindowTitle('Tables Demo')
        self.setGeometry(100, 100, 500, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TablesDemo()
    sys.exit(app.exec_())
