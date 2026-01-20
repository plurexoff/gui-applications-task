"""
Калкулятор - приложение PyQt5
Это апрованое но момическое оно демонстрирует:
- Кнопки для нажатие
- Обработку событий
- Отображение результатов
- GridLayout
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit, QLabel
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Calculator(QMainWindow):
    """КалкуляторНое приложение"""
    
    def __init__(self):
        super().__init__()
        self.expression = ''
        self.initUI()
    
    def initUI(self):
        """Инициализация интерфейса"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # Надпись
        title = QLabel('Калкулятор')
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        main_layout.addWidget(title)
        
        # Дисплей
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        display_font = QFont()
        display_font.setPointSize(24)
        self.display.setFont(display_font)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("QLineEdit { padding: 10px; border: 2px solid #333; }")
        main_layout.addWidget(self.display)
        
        # Grid layout для кнопок
        grid_layout = QGridLayout()
        
        # Определение кнопок
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('÷', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]
        
        # Добавление кнопок в grid
        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setFont(QFont('Arial', 14))
            button.setMinimumHeight(60)
            
            # Настройка стилей
            if text in ['+', '-', '*', '÷', '=']:
                button.setStyleSheet("QPushButton { background-color: #ff9500; color: white; font-weight: bold; }")
            else:
                button.setStyleSheet("QPushButton { background-color: #f0f0f0; }")
            
            # Подключение обработчика
            if text == '=':
                button.clicked.connect(self.on_equals)
            else:
                button.clicked.connect(lambda checked, t=text: self.on_button_clicked(t))
            
            grid_layout.addWidget(button, row, col)
        
        # Кнопка "Очистить"
        clear_button = QPushButton('Очистить')
        clear_button.setFont(QFont('Arial', 12))
        clear_button.setMinimumHeight(50)
        clear_button.setStyleSheet("QPushButton { background-color: #ff3b30; color: white; }")
        clear_button.clicked.connect(self.on_clear)
        grid_layout.addWidget(clear_button, 4, 0, 1, 4)
        
        main_layout.addLayout(grid_layout)
        central_widget.setLayout(main_layout)
        
        # Параметры окна
        self.setWindowTitle('Калкулятор')
        self.setGeometry(100, 100, 400, 500)
        self.show()
    
    def on_button_clicked(self, text):
        """Обработъик нажатия кнопки с цифрой или оператором"""
        # Обработка деления
        if text == '÷':
            text = '/'
        
        self.expression += text
        self.display.setText(self.expression)
    
    def on_equals(self):
        """Обработчик нажатия кнопки '='"""
        try:
            # Вычисление результата
            result = eval(self.expression)
            self.display.setText(str(result))
            self.expression = str(result)
        except:
            self.display.setText('Ошибка')
            self.expression = ''
    
    def on_clear(self):
        """Обработчик нажатия кнопки 'Очистить'"""
        self.expression = ''
        self.display.setText('')
    
    def keyPressEvent(self, event):
        """Обработчик клавиш клавиатуры"""
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.on_equals()
        elif event.key() == Qt.Key_Backspace:
            self.expression = self.expression[:-1]
            self.display.setText(self.expression)
        elif event.key() == Qt.Key_Escape:
            self.on_clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())
