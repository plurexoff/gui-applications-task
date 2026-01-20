# Быстрый старт

## Установка

```bash
pip install PyQt5
```

## Запуск аппликаций

### 1. Лаунчер (Основное меню)

```bash
python main.py
```

### 2. Калкулятор

```bash
python run_calculator.py
```

### 3. Todo приложение

```bash
python run_todo.py
```

### 4. Примеры

```bash
# Простое окно
python examples/basic_window.py

# Сигналы и слоты
python examples/signals_slots.py

# Лайауты
python examples/layouts.py

# Настройка стилей
python examples/styling.py

# Таблицы
python examples/tables.py

# Меню и тулбары
python examples/menus.py
```

## Основные концепции

### Виджеты

✓ QPushButton  
✓ QLineEdit  
✓ QLabel  
✓ QComboBox  
✓ QCheckBox  
✓ QSpinBox  
✓ QSlider  
✓ QTableWidget  
✓ QListWidget  

### Лайауты

✓ QVBoxLayout  
✓ QHBoxLayout  
✓ QGridLayout  
✓ QFormLayout  

### Сигналы и слоты

```python
# Подключение сигнала
button.clicked.connect(self.handler)

# Основные сигналы
button.clicked.connect()
line_edit.textChanged.connect()
slider.valueChanged.connect()
checkbox.stateChanged.connect()
```

## Пример: Простое окно

```python
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel
)

class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        label = QLabel('Привет!')
        layout.addWidget(label)
        
        button = QPushButton('Кнопка')
        button.clicked.connect(self.on_click)
        layout.addWidget(button)
        
        central_widget.setLayout(layout)
        
        self.setWindowTitle('Простое окно')
        self.setGeometry(100, 100, 300, 200)
        self.show()
    
    def on_click(self):
        print('Нажата!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleApp()
    sys.exit(app.exec_())
```

## Тестирование

```bash
pytest tests/ -v
```
