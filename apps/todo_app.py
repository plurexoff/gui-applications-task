"""
Todo Application - PyQt5
Основные функции:
- Добавление задач
- Пометка выполненных
- Удаление задач
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QListWidget, QListWidgetItem, QLabel
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class TodoApp(QMainWindow):
    """Todo application"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Initialize UI"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel('Мои дела')
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        main_layout.addWidget(title)
        
        # Input
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Введите новую задачу...')
        add_button = QPushButton('Добавить')
        add_button.clicked.connect(self.add_task)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(add_button)
        main_layout.addLayout(input_layout)
        
        # List
        self.task_list = QListWidget()
        self.task_list.itemDoubleClicked.connect(self.toggle_task)
        main_layout.addWidget(self.task_list)
        
        # Buttons
        button_layout = QHBoxLayout()
        delete_button = QPushButton('Удалить')
        delete_button.clicked.connect(self.delete_task)
        button_layout.addWidget(delete_button)
        main_layout.addLayout(button_layout)
        
        central_widget.setLayout(main_layout)
        
        self.setWindowTitle('Мои дела')
        self.setGeometry(100, 100, 400, 500)
        self.show()
    
    def add_task(self):
        """Add new task"""
        text = self.input_field.text().strip()
        if text:
            item = QListWidgetItem(text)
            item.setCheckState(Qt.Unchecked)
            self.task_list.addItem(item)
            self.input_field.clear()
    
    def toggle_task(self):
        """Toggle task completion"""
        item = self.task_list.currentItem()
        if item:
            if item.checkState() == Qt.Unchecked:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
    
    def delete_task(self):
        """Delete selected task"""
        item = self.task_list.currentItem()
        if item:
            self.task_list.takeItem(self.task_list.row(item))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo = TodoApp()
    sys.exit(app.exec_())
