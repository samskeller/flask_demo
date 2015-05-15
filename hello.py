from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'

@app.route('/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
