"""
Tests for widgets
"""
import pytest
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

# Create QApplication for testing
app = QApplication.instance() or QApplication(sys.argv)


class TestWidgets:
    """Test basic widgets"""
    
    def test_button_click(self):
        """Test button click signal"""
        button = QPushButton('Test')
        clicked = []
        button.clicked.connect(lambda: clicked.append(True))
        button.click()
        assert clicked
    
    def test_line_edit(self):
        """Test line edit"""
        line_edit = QLineEdit()
        line_edit.setText('Hello')
        assert line_edit.text() == 'Hello'
    
    def test_line_edit_clear(self):
        """Test line edit clear"""
        line_edit = QLineEdit()
        line_edit.setText('Hello')
        line_edit.clear()
        assert line_edit.text() == ''
