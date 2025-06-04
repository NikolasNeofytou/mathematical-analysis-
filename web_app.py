from flask import Flask, render_template_string, request
from calculus_solver import parse_expression, solve_expression

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>Calculus Solver</title>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <h1>Calculus Solver</h1>
    <form method="post">
        <input id="expr" type="text" name="expr" size="50" value="{{expr|e}}" placeholder="Enter LaTeX expression" oninput="updatePreview()"/>
        <button type="submit">Solve</button>
    </form>
    <div id="preview"></div>
    <script>
        function updatePreview() {
            var el = document.getElementById('expr');
            var preview = document.getElementById('preview');
            preview.textContent = '$$' + el.value + '$$';
            if (window.MathJax) {
                MathJax.typesetPromise();
            }
        }
        document.addEventListener('DOMContentLoaded', updatePreview);
    </script>
    {% if solution %}
        <div id="solution">
        {% for line in solution.split('\n') %}
            <p>{{ line | safe }}</p>
        {% endfor %}
        </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    expr = ''
    solution = None
    if request.method == 'POST':
        expr = request.form.get('expr', '')
        try:
            parsed = parse_expression(expr)
            solution = solve_expression(parsed)
        except Exception as exc:
            solution = f"Error: {exc}"
    return render_template_string(PAGE, expr=expr, solution=solution)

if __name__ == '__main__':
    app.run(debug=True)
