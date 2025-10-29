from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello, Flask!"

# Example route with parameters
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

# Example POST route
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Form submitted! Hello, {name}"
    return '''
        <form method="POST">
            Name: <input type="text" name="name">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
