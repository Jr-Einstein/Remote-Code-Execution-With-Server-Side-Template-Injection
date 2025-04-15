from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Live demonstrations</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(120deg, #d0e8f2, #ffffff);
        }
        .navbar {
            background-color: #3f51b5;
            padding: 20px;
            color: white;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .container {
            max-width: 960px;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        .header {
            display: flex;
            align-items: center;
        }
        .logo {
            height: 80px;
            margin-right: 20px;
        }
        h1 {
            color: #333;
            font-size: 28px;
            margin: 0;
        }
        .badge {
            background-color: #28a745;
            color: white;
            padding: 4px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-left: 10px;
        }
        .output {
            background: #f1f1f1;
            padding: 20px;
            border-radius: 8px;
            margin-top: 30px;
            font-family: monospace;
            white-space: pre-wrap;
            word-break: break-word;
        }
        .instructions {
            font-size: 16px;
            color: #666;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class=\"navbar\">Live demonstrations</div>
    <div class=\"container\">
        <div class=\"header\">
            <img src=\"https://owasp.org/www-project-skf/assets/images/logo.svg\" class=\"logo\" alt=\"OWASP SKF\">
            <div>
                <h1>Live demonstration! <span class=\"badge\">Server side template injection!</span></h1>
                <div class=\"instructions\">Inject Jinja2 payload directly into the URL to see results!</div>
            </div>
        </div>
        <div class=\"output\">
            <strong>URL:</strong> {{ url }}<br><br>
            <strong>Evaluated Output:</strong><br>{{ result }}
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return '''<h2>Usage:</h2>
              <p>Pass the payload in the URL like: <code>http://127.0.0.1:5000/{{7*7}}</code></p>'''

@app.route('/<path:payload>')
def ssti(payload):
    decoded_payload = request.path[1:]  # strip leading slash
    try:
        result = render_template_string(decoded_payload)
    except Exception as e:
        result = f"Error: {e}"
    return render_template_string(TEMPLATE, url=request.url, result=result)

if __name__ == '__main__':
    app.run(debug=True)

