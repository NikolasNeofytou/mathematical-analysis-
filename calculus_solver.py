import sys
import sympy as sp
from sympy.parsing.latex import parse_latex


def parse_expression(expr_str: str):
    try:
        return parse_latex(expr_str)
    except Exception:
        return sp.sympify(expr_str)


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
    expr = parse_expression(expr_str)
    solution = solve_expression(expr)
    print(solution)


if __name__ == "__main__":
    main()
