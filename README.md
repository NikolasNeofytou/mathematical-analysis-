# mathematical-analysis-

This repository provides a simple calculus solver. The solver can evaluate
LaTeX expressions representing derivatives, integrals and summations.

## Usage

Run the solver from the command line and pass a LaTeX expression in quotes.
Examples:

```bash
python calculus_solver.py "\\frac{d}{dx} x^2"
python calculus_solver.py "\\int x^2 dx"
python calculus_solver.py "\\sum_{n=1}^5 n^2"
```

The script prints a few steps and the final result in LaTeX format.
