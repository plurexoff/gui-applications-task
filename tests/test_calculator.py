"""
Tests for calculator
"""
import pytest


def evaluate_expression(expr):
    """Evaluate mathematical expression"""
    try:
        return eval(expr)
    except:
        return None


class TestCalculator:
    """Test calculator functionality"""
    
    def test_simple_addition(self):
        """Test simple addition"""
        result = evaluate_expression('2+3')
        assert result == 5
    
    def test_simple_subtraction(self):
        """Test simple subtraction"""
        result = evaluate_expression('5-3')
        assert result == 2
    
    def test_simple_multiplication(self):
        """Test simple multiplication"""
        result = evaluate_expression('4*5')
        assert result == 20
    
    def test_simple_division(self):
        """Test simple division"""
        result = evaluate_expression('10/2')
        assert result == 5
    
    def test_complex_expression(self):
        """Test complex expression"""
        result = evaluate_expression('2+3*4')
        assert result == 14
    
    def test_invalid_expression(self):
        """Test invalid expression"""
        result = evaluate_expression('2++3')
        assert result is None
