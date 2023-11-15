from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/get_something')
def get_something():
    return {'dictionary1':'to handle the json'}


if __name__ == "__main__":
    app.run(host = '127.0.0.1' , port=5000)
