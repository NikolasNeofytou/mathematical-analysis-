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

## Web application

A minimal Flask app provides a web interface for entering equations. Start the server with:

```bash
python web_app.py
```

Open `http://localhost:5000` in a browser to enter a LaTeX expression and view the step-by-step solution rendered with MathJax.

Install dependencies using `pip install -r requirements.txt` if needed.
