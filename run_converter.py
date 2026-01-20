#!/usr/bin/env python3
"""
Запуск конвертера
"""
import sys
from examples.styling import StylingDemo
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StylingDemo()
    sys.exit(app.exec_())
