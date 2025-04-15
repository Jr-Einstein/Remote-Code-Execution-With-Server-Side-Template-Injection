from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>SSTI Demo</h2>
        <form action="/vulnerable" method="post">
            <input name="payload" placeholder="Enter SSTI Payload" size="50">
            <input type="submit" value="Test">
        </form>
    '''

@app.route('/vulnerable', methods=['POST'])
def vulnerable():
    payload = request.form['payload']
    try:
        output = render_template_string(payload)
    except Exception as e:
        output = f"Error: {e}"
    return f"<h3>Output:</h3><pre>{output}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
