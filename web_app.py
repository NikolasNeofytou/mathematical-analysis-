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
    <style>
        body { background:#111; color:#eee; font-family: Arial, sans-serif; margin:0; }
        .container { width:80%; max-width:800px; margin:2em auto; }
        header { text-align:center; margin-bottom:1em; }
        h1 { margin:0; color:#4dd0e1; }
        form { display:flex; flex-direction:column; align-items:stretch; }
        input[type=text] { padding:0.5em; margin-bottom:0.5em; background:#222; color:#eee; border:1px solid #555; }
        button { padding:0.5em 1em; margin-top:0.5em; }
        .toolbar { margin-bottom:0.5em; }
        .toolbar button { margin-right:0.2em; }
        .step { border:1px solid #555; background:#222; padding:0.5em; border-radius:4px; margin-top:0.5em; }
        #preview { margin-top:0.5em; }
    </style>
    <script>
        function insert(text) {
            var el = document.getElementById('expr');
            var start = el.selectionStart;
            var end = el.selectionEnd;
            el.value = el.value.slice(0, start) + text + el.value.slice(end);
            el.focus();
            el.selectionStart = el.selectionEnd = start + text.length;
            updatePreview();
        }
        function fixLatex(str) {
            var tokens = ['int', 'sum', 'sqrt', 'frac', 'lim'];
            tokens.forEach(function(t) {
                var re = new RegExp('(^|[^\\\\])' + t, 'g');
                str = str.replace(re, '$1\\\' + t);
            });
            return str;
        }
        function prepareForm() {
            var el = document.getElementById('expr');
            el.value = fixLatex(el.value);
            updatePreview();
        }
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
</head>
<body>
    <div class="container">
        <header><h1>Calculus Solver</h1></header>
        <form method="post" onsubmit="prepareForm()">
            <div class="toolbar">
                <button type="button" onclick="insert('\\frac{d}{dx} ')">d/dx</button>
                <button type="button" onclick="insert('\\int ')">&#8747;</button>
                <button type="button" onclick="insert('\\sum_{n=1}^{ } ')">&#8721;</button>
                <button type="button" onclick="insert('^{}')">^</button>
                <button type="button" onclick="insert('\\sqrt{}')">sqrt</button>
            </div>
            <input id="expr" type="text" name="expr" value="{{expr|e}}" placeholder="\\int_0^1 x dx" oninput="updatePreview()" />
            <button type="submit">Solve</button>
        </form>
        <div id="preview"></div>
        {% if solution %}
        <div id="solution" style="margin-top:1em;">
            {% if solution.startswith('Error:') %}
                <p style="color:red;">{{ solution }}</p>
            {% else %}
                {% for line in solution.split('\n') %}
                    <div class="step">{{ line | safe }}</div>
                {% endfor %}
            {% endif %}
        </div>
        {% endif %}
    </div>
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
