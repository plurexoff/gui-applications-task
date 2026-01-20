#!/usr/bin/env python3
"""
Запуск примера: Нотпад
"""
import sys
from examples.basic_window import SimpleWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleWindow()
    sys.exit(app.exec_())
