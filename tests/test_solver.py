import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from calculus_solver import parse_expression, solve_expression


def test_derivative():
    expr = parse_expression("\\frac{d}{dx} x^2")
    result = solve_expression(expr)
    assert "2 x" in result


def test_integral():
    expr = parse_expression("\\int x dx")
    result = solve_expression(expr)
    assert "\\frac{x^{2}}{2}" in result


def test_sum():
    expr = parse_expression("\\sum_{n=1}^3 n")
    result = solve_expression(expr)
    assert "6" in result
