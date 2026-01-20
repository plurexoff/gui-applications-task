"""
Пример 2: Сигналы и слоты
Основной механизм связи между объектами в PyQt5
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QSlider, QSpinBox
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


class SignalsDemo(QMainWindow):
    """Demo signals and slots"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Initialize UI"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel('Сигналы и слоты')
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        main_layout.addWidget(title)
        
        # Slider
        slider_layout = QHBoxLayout()
        slider_label = QLabel('Ползунок:')
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.sliderMoved.connect(self.on_slider_moved)
        slider_layout.addWidget(slider_label)
        slider_layout.addWidget(self.slider)
        main_layout.addLayout(slider_layout)
        
        # SpinBox
        spinbox_layout = QHBoxLayout()
        spinbox_label = QLabel('Число:')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(100)
        self.spinbox.valueChanged.connect(self.on_spinbox_changed)
        spinbox_layout.addWidget(spinbox_label)
        spinbox_layout.addWidget(self.spinbox)
        main_layout.addLayout(spinbox_layout)
        
        # Result
        self.result_label = QLabel('Нажмите кнопки')
        self.result_label.setStyleSheet("border: 1px solid gray; padding: 10px;")
        main_layout.addWidget(self.result_label)
        
        # Button with custom signal
        button = QPushButton('Кликните меня')
        button.clicked.connect(self.on_button_clicked)
        main_layout.addWidget(button)
        
        central_widget.setLayout(main_layout)
        
        self.setWindowTitle('Сигналы и слоты')
        self.setGeometry(100, 100, 500, 300)
        self.show()
    
    def on_slider_moved(self):
        """Handle slider movement"""
        value = self.slider.value()
        self.spinbox.blockSignals(True)
        self.spinbox.setValue(value)
        self.spinbox.blockSignals(False)
        self.result_label.setText(f'Ползунок: {value}')
    
    def on_spinbox_changed(self):
        """Handle spinbox value change"""
        value = self.spinbox.value()
        self.slider.blockSignals(True)
        self.slider.setValue(value)
        self.slider.blockSignals(False)
        self.result_label.setText(f'Число: {value}')
    
    def on_button_clicked(self):
        """Handle button click"""
        self.result_label.setText('Кнопка нажата!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignalsDemo()
    sys.exit(app.exec_())
