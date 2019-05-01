from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #render_templte是渲染模板，（通传入的关键字参数，替换模板中的变量）
    return render_template('index.html' , name=__name, movies=__movies)

@app.route('/<name>')
def hello_name(name):
    return "Hello %s" %name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='minu'))
    return "Test Page url_for 执行失败"

#错误处理函数
@app.errorhandler(404)
def error_404(e):
    return '404 Error',404

#实际内容，用于模板中变量的替换
__name = 'minu'
__movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]



if __name__ == '__main__':
    app.debug = True
    app.run()
