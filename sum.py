from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/add")
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return str(a + b)
    except ValueError:
        return "Invalid numbers", 400
        
if __name__ == '__main__':
    # debug=False prevents auto-restart in CI
    app.run(debug=False, host='127.0.0.1', port=5000)
