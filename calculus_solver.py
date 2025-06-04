import sys
import sympy as sp
from sympy.parsing.latex import parse_latex


class ParseError(Exception):
    """Raised when an input string cannot be parsed as a math expression."""


def parse_expression(expr_str: str) -> sp.Expr:
    """Parse ``expr_str`` into a SymPy expression.

    The function first attempts to interpret the input as LaTeX.  If this fails
    it falls back to ``sympify`` which understands basic SymPy syntax.  When
    both attempts fail a ``ParseError`` with a descriptive message is raised.
    """

    try:
        return parse_latex(expr_str)
    except Exception as latex_error:
        try:
            return sp.sympify(expr_str)
        except Exception as sympy_error:
            raise ParseError(
                "Could not parse expression as LaTeX or SymPy syntax. "
                "Check for missing braces or unsupported commands."
            ) from latex_error


def solve_expression(expr: sp.Expr) -> str:
    if isinstance(expr, sp.Integral):
        result = sp.integrate(expr.function, *expr.limits)
        latex_expr = sp.latex(expr)
        latex_result = sp.latex(result)
        steps = [f"Given integral $${latex_expr}$$", f"Evaluating the integral:", f"$$ {latex_result} $$ + C"]
        return "\n".join(steps)
    elif isinstance(expr, sp.Derivative):
        result = expr.doit()
        latex_expr = sp.latex(expr)
        latex_result = sp.latex(result)
        steps = [f"Given derivative $${latex_expr}$$", f"Computing the derivative:", f"$$ {latex_result} $$"]
        return "\n".join(steps)
    elif isinstance(expr, sp.Sum):
        result = expr.doit()
        latex_expr = sp.latex(expr)
        latex_result = sp.latex(result)
        steps = [f"Given sum $${latex_expr}$$", f"Evaluating the sum:", f"$$ {latex_result} $$"]
        return "\n".join(steps)
    else:
        raise ValueError("Unsupported expression type")


def main():
    if len(sys.argv) < 2:
        print('Usage: python calculus_solver.py "<latex expression>"')
        return
    expr_str = sys.argv[1]
    try:
        expr = parse_expression(expr_str)
        solution = solve_expression(expr)
    except ParseError as err:
        print(f"Error: {err}")
        return
    except Exception as err:
        print(f"Failed to solve expression: {err}")
        return
    print(solution)


if __name__ == "__main__":
    main()
