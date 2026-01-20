"""
Основное меню – лаунчер для всех аппликаций
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PyQt5.QtGui import QFont
from apps.calculator import Calculator
from apps.todo_app import TodoApp


class AppLauncher(QMainWindow):
    """Лаунчер аппликаций"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Инициализация интерфейса"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Заголовок
        title = QLabel('Графические Приложения PyQt5')
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Описание
        description = QLabel(
            'Выберите приложение для запуска:\n'
        )
        layout.addWidget(description)
        
        # Калкулятор
        calculator_button = QPushButton('🧠 Калкулятор')
        calculator_button.setMinimumHeight(50)
        calculator_button.setStyleSheet(
            "QPushButton { background-color: #4CAF50; color: white; "
            "font-size: 14px; font-weight: bold; border-radius: 5px; }"
        )
        calculator_button.clicked.connect(self.launch_calculator)
        layout.addWidget(calculator_button)
        
        # Todo аппликация
        todo_button = QPushButton('📚 Мои дела')
        todo_button.setMinimumHeight(50)
        todo_button.setStyleSheet(
            "QPushButton { background-color: #2196F3; color: white; "
            "font-size: 14px; font-weight: bold; border-radius: 5px; }"
        )
        todo_button.clicked.connect(self.launch_todo)
        layout.addWidget(todo_button)
        
        # О приложении
        about_button = QPushButton('ℹ️ О программе')
        about_button.setMinimumHeight(50)
        about_button.setStyleSheet(
            "QPushButton { background-color: #FF9800; color: white; "
            "font-size: 14px; font-weight: bold; border-radius: 5px; }"
        )
        about_button.clicked.connect(self.show_about)
        layout.addWidget(about_button)
        
        # Выход
        exit_button = QPushButton('❌ Выход')
        exit_button.setMinimumHeight(50)
        exit_button.setStyleSheet(
            "QPushButton { background-color: #f44336; color: white; "
            "font-size: 14px; font-weight: bold; border-radius: 5px; }"
        )
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)
        
        central_widget.setLayout(layout)
        
        # Параметры окна
        self.setWindowTitle('Приложения PyQt5')
        self.setGeometry(200, 200, 400, 400)
        self.show()
    
    def launch_calculator(self):
        """Лаунч калкулятора"""
        self.calculator = Calculator()
    
    def launch_todo(self):
        """Лаунч todo аппликации"""
        self.todo = TodoApp()
    
    def show_about(self):
        """О программе"""
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(
            self,
            'О программе',
            'Приложения PyQt5\n\n'
            'Задание #4: Научиться составлять графические '
            'интерфейсы\n\n'
            '📚 Приложения: \n'
            '- Калкулятор\n'
            '- Мои дела\n'
            '- Нотпад\n'
            '- и ещё много...'
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = AppLauncher()
    sys.exit(app.exec_())
