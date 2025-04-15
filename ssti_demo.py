from flask import Flask, request
from jinja2 import Template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        input_data = request.form.get("input", "")
        template = Template(f"Welcome back, {input_data}")  # Vulnerable line
        result = template.render()

    return f"""
    <html>
    <head>
        <title>Secure PayBank</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #f3f3f3, #dce2f0);
                color: #333;
                padding: 40px;
            }}
            .container {{
                background: white;
                border-radius: 12px;
                padding: 30px;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
                max-width: 600px;
                margin: auto;
                text-align: center;
            }}
            input {{
                padding: 10px;
                margin-top: 10px;
                width: 80%;
                font-size: 16px;
            }}
            button {{
                padding: 10px 20px;
                font-size: 16px;
                background: #007BFF;
                color: white;
                border: none;
                margin-top: 10px;
                cursor: pointer;
                border-radius: 5px;
            }}
            .url-display {{
                margin-top: 20px;
                background: #f7f7f7;
                padding: 10px;
                font-family: monospace;
                border-radius: 5px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/OOjs_UI_icon_lock-ltr-progressive.svg/1024px-OOjs_UI_icon_lock-ltr-progressive.svg.png" width="60"/>
            <h2>Welcome to Secure PayBank</h2>
            <p>Enter your name to continue:</p>
            <form method="POST">
                <input name="input" placeholder="e.g. Aman or {{7*7}}" required>
                <br>
                <button type="submit">Continue</button>
            </form>
            <div class="url-display">Current URL: http://127.0.0.1:5000/</div>
            <h3>{result}</h3>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)
