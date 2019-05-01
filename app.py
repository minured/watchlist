from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to My Watchlist!6666"

@app.route('/<name>')
def hello_name(name):
    return "Hello %s" %name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='minu'))
    return "Test Page url_for 执行失败"


if __name__ == '__main__':
    app.debug = True
    app.run()
