"""
Пример 5: Меню и тулбары
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
)
from PyQt5.QtGui import QFont


class MenusDemo(QMainWindow):
    """Menus demonstration"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Initialize UI"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        title = QLabel('Меню и тулбары')
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Create menu bar
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('Файл')
        new_action = file_menu.addAction('Новый')
        new_action.triggered.connect(lambda: print('Новый файл'))
        open_action = file_menu.addAction('Открыть')
        open_action.triggered.connect(lambda: print('Открыть файл'))
        file_menu.addSeparator()
        exit_action = file_menu.addAction('Выход')
        exit_action.triggered.connect(self.close)
        
        # Edit menu
        edit_menu = menubar.addMenu('Редактирование')
        undo_action = edit_menu.addAction('Отменить')
        undo_action.triggered.connect(lambda: print('Отмена'))
        redo_action = edit_menu.addAction('Повторить')
        redo_action.triggered.connect(lambda: print('Повтор'))
        
        # Help menu
        help_menu = menubar.addMenu('О программе')
        about_action = help_menu.addAction('О программе')
        about_action.triggered.connect(lambda: print('О программе'))
        
        central_widget.setLayout(layout)
        
        self.setWindowTitle('Menus Demo')
        self.setGeometry(100, 100, 400, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MenusDemo()
    sys.exit(app.exec_())
