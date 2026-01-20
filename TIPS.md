# Полезные советы и трики

## 1. Конекторы (Signals & Slots)

```python
# связываем сигнал с методом
button.clicked.connect(self.on_button_clicked)

# Можно также использовать ламбды
button.clicked.connect(lambda: self.on_click(some_param))

# Неразрываем сигналы для исключения рекурсии
combobox.blockSignals(True)
combobox.setCurrentIndex(5)
combobox.blockSignals(False)
```

## 2. Настройка стилей

```python
# Qt Style Sheets (QSS) - наподобие CSS
button.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QPushButton:pressed {
        background-color: #3d8b40;
    }
""")

# Применить стили в строке
button.setStyleSheet("background-color: red; color: white;")
```

## 3. Полючение данных из виджетов

```python
# QLineEdit
text = self.line_edit.text()  # получить текст

# QSpinBox
value = self.spinbox.value()  # получить число

# QCheckBox
checked = self.checkbox.isChecked()  # проверить

# QComboBox
selected = self.combobox.currentText()  # выбранный элемент

# QTableWidget
item = self.table.item(row, col)
text = item.text()
```

## 4. Отображение сообщений

```python
from PyQt5.QtWidgets import QMessageBox

# Информация
QMessageBox.information(self, 'Титл', 'Сообщение')

# Предупреждение
QMessageBox.warning(self, 'Предупреждение', 'Текст')

# Ошибка
QMessageBox.critical(self, 'Ошибка', 'Ошибка!')

# Наопрос
reply = QMessageBox.question(
    self, 'Вопрос', 'Вы уверены?',
    QMessageBox.Yes | QMessageBox.No
)
```

## 5. Организация элементов

```python
from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QGridLayout
)

# Вертикальный layout
vbox = QVBoxLayout()
vbox.addWidget(label1)
vbox.addWidget(label2)

# Горизонтальный layout
hbox = QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)

# Грид layout
grid = QGridLayout()
grid.addWidget(widget1, 0, 0)  # row, col
grid.addWidget(widget2, 0, 1)
grid.addWidget(widget3, 1, 0)

# Нестинг
main_layout = QVBoxLayout()
main_layout.addLayout(hbox)
main_layout.addLayout(grid)
```

## 6. Настройка фонтов

```python
from PyQt5.QtGui import QFont

# Основное беременная
font = QFont()
font.setPointSize(14)
font.setBold(True)
font.setItalic(True)
label.setFont(font)

# Короткая альтернатива
label.setFont(QFont('Arial', 12, QFont.Bold))
```

## 7. Обработка клавиш

```python
from PyQt5.QtCore import Qt

def keyPressEvent(self, event):
    if event.key() == Qt.Key_Return:
        self.on_enter_pressed()
    elif event.key() == Qt.Key_Escape:
        self.close()
```

## 8. Оптимизация

```python
# Не персчитывать все данные
self.list_widget.setUpdatesEnabled(False)
# ... несколько операций ...
self.list_widget.setUpdatesEnabled(True)

# Превент сигналов
self.slider.blockSignals(True)
self.slider.setValue(50)
self.slider.blockSignals(False)
```
