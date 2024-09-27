from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, DevOps!"

@app.route('/devops')
def devops():
    return "Rota DevOps!"

@app.route('/about')
def about():
    return "Rota about!"

@app.route('/contact')
def contact():
    return "Rota contact!"

@app.route('/non-existent-page')
def nonExistent():
    return "Rota non-existent-page!"

@app.route('/login')
def nonExistent():
    return "Rota login!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
