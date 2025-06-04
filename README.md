# mathematical-analysis-

This repository provides a simple calculus solver. The solver can evaluate LaTeX expressions representing derivatives, integrals and summations.

## Command line usage

Run the solver from the command line and pass a LaTeX expression in quotes. Examples:

```bash
python calculus_solver.py "\\frac{d}{dx} x^2"
python calculus_solver.py "\\int x^2 dx"
python calculus_solver.py "\\sum_{n=1}^5 n^2"
```

The script prints a few steps and the final result in LaTeX format.

## Input format

Provide raw LaTeX without surrounding dollar signs. The solver understands
standard calculus constructs such as:

- Derivatives using `\frac{d}{dx}` or `\frac{\partial}{\partial x}`
- Integrals in the form `\int expression dx`
- Finite sums using `\sum_{n=1}^{N} expression`

For example `\frac{d}{dx} x^2`, `\int x^2 dx` or `\sum_{n=1}^3 n`.

If the program cannot parse your input, it will report an error explaining what
went wrong so you can adjust the expression.

## Web application

A minimal Flask app provides a web interface for entering equations. Start the server with:

```bash
python web_app.py
```

Open `http://localhost:5000` in a browser and enter a LaTeX expression using the
same format as on the command line (omit surrounding `$` markers).  The page
shows a live preview of your input using MathJax.

If parsing fails, a helpful error message is displayed.  Typical mistakes
include missing braces or leaving out the integration variable.

Install dependencies using `pip install -r requirements.txt` if needed.
