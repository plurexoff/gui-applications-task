"""
Пример 1: Простое окно с PyQt5
Все стандартные виджеты PyQt5
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon


class SimpleWindow(QMainWindow):
    """Простое окно приложения"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Инициализация интерфейса"""
        # Создание главного виджета
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Создание вертикального layout
        main_layout = QVBoxLayout()
        
        # Заголовок
        title = QLabel('Простое приложение PyQt5')
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        main_layout.addWidget(title)
        
        # Горизонтальный layout для ввода
        input_layout = QHBoxLayout()
        input_label = QLabel('Введите текст:')
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Введите что-нибудь...')
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_field)
        main_layout.addLayout(input_layout)
        
        # Горизонтальный layout для кнопок
        button_layout = QHBoxLayout()
        
        # Кнопка "Показать"
        show_button = QPushButton('Показать')
        show_button.clicked.connect(self.on_show_button_clicked)
        button_layout.addWidget(show_button)
        
        # Кнопка "Очистить"
        clear_button = QPushButton('Очистить')
        clear_button.clicked.connect(self.on_clear_button_clicked)
        button_layout.addWidget(clear_button)
        
        # Кнопка "Выход"
        exit_button = QPushButton('Выход')
        exit_button.clicked.connect(self.close)
        button_layout.addWidget(exit_button)
        
        main_layout.addLayout(button_layout)
        
        # Метка результата
        self.result_label = QLabel('Результат будет здесь')
        self.result_label.setStyleSheet(
            "border: 1px solid gray; padding: 10px; background-color: #f0f0f0;"
        )
        main_layout.addWidget(self.result_label)
        
        # Добавление основного layout в центральный виджет
        central_widget.setLayout(main_layout)
        
        # Параметры окна
        self.setWindowTitle('Простое окно PyQt5')
        self.setGeometry(100, 100, 500, 300)
        self.show()
    
    def on_show_button_clicked(self):
        """Обработчик нажатия кнопки 'Показать'"""
        text = self.input_field.text()
        if text:
            self.result_label.setText(f'Вы ввели: {text}')
            QMessageBox.information(self, 'Информация', f'Текст: {text}')
        else:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите текст!')
    
    def on_clear_button_clicked(self):
        """Обработчик нажатия кнопки 'Очистить'"""
        self.input_field.clear()
        self.result_label.setText('Результат будет здесь')
    
    def keyPressEvent(self, event):
        """Обработчик нажатия клавиш"""
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.on_show_button_clicked()
        elif event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleWindow()
    sys.exit(app.exec_())
