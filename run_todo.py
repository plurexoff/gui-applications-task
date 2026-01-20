#!/usr/bin/env python3
"""
Запуск Todo приложения
"""
import sys
from apps.todo_app import TodoApp
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo = TodoApp()
    sys.exit(app.exec_())
