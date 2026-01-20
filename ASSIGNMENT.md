# Задание №4: Графический интерфейс (GUI)

## Описание задания

Необходимо создать практические оконные приложения с элементами графического интерфейса.

## Требования

### 1. Основные виджеты

**PyQt5** обеспечивает:

- **QMainWindow** - Основное окно аппликации
- **QWidget** - Основной родитель
- **QPushButton** - Кнопка
- **QLineEdit** - Однострочное поле ввода
- **QTextEdit** - Многострочный поле ввода
- **QLabel** - Надпись
- **QComboBox** - Окно выбора
- **QCheckBox** - Проверяющая ячейка
- **QSpinBox** - Поле числового ввода
- **QSlider** - Ползунок
- **QTableWidget** - Таблица

### 2. Лайауты (Организация)

- **QVBoxLayout** - Вертикальное расположение
- **QHBoxLayout** - Горизонтальное расположение
- **QGridLayout** - Грид
- **QFormLayout** - Форма

### 3. Сигналы и слоты

```python
# Сигнал - это особые триггеры события
button.clicked.connect(self.on_button_clicked)

# Слот - это метод, который вызывается при сигнале
def on_button_clicked(self):
    print('Button clicked!')
```

### 4. Обработка событий

```python
# Обычные сигналы
button.clicked.connect(self.handler)
line_edit.textChanged.connect(self.on_text_changed)
slider.valueChanged.connect(self.on_value_changed)
checkbox.stateChanged.connect(self.on_state_changed)
```

### 5. Отображение резултатов

```python
# Настоящее отображение
self.label.setText(result)

# Мессэдж бокс
QMessageBox.information(self, 'Титл', 'Сообщение')
QMessageBox.warning(self, 'Предупреждение', 'Текст')
QMessageBox.critical(self, 'Ошибка', 'Ошибка!')
```

## Пример: Простое окно

```python
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
)

class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Label
        label = QLabel('Нажмите кнопку')
        layout.addWidget(label)
        
        # Button
        button = QPushButton('Кнопка')
        button.clicked.connect(self.on_click)
        layout.addWidget(button)
        
        central_widget.setLayout(layout)
        
        self.setWindowTitle('Простое окно')
        self.setGeometry(100, 100, 300, 200)
        self.show()
    
    def on_click(self):
        print('Кнопка нажата!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleApp()
    sys.exit(app.exec_())
```

## Приложения в этом проекте

### 1. **Калкулятор**
- Кнопки и дисплей
- GridLayout
- Обработка математических выражений

### 2. **Todo Приложение**
- QLineEdit для ввода
- QListWidget для списка
- QPushButton для действий

### 3. **Нотпад**
- QTextEdit для редактирования
- Меню и тулбар

## Установка

```bash
pip install PyQt5
```

## Запуск

```bash
# Целая аппликация
python apps/calculator.py

# Пример
python examples/basic_window.py
```

## Ключевые концепции

✓ Окна и диалоги  
✓ Виджеты и организация  
✓ Сигналы и слоты  
✓ Обработка событий  
✓ Настройка стилей  
✓ Отображение результатов  
