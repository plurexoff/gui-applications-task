#!/usr/bin/env python3
"""
Запуск калкулятора
"""
import sys
from apps.calculator import Calculator
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())
