from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy #导入扩展类（数据库工具orm）
#orm对象关系映射，借助SQLAlchemy可以通过
#定义pyhton类来表示数据库里的一张表（类属型 表示表中的 字段/列）
#通过对这个类的各种操作来代替写sql语句，
import os
import click

app = Flask(__name__)
db = SQLAlchemy(app) #初始化


#app.root_path 返回程序实例所在模块的路径（目前来说，即项目根目录）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path,'data.db')

@app.route('/')
def index():

    #从数据库中读取数据
    user = User.query.first() #读取用户记录
    movies = Movie.query.all() #读取所有电影

    #render_templte是渲染模板，（通传入的关键字参数，替换模板中的变量）
    #给index传入数据库中的数据
    return render_template('index.html', user = user, movies=movies)

    # return render_template('index.html' , name=_name, movies=_movies) #本模块中的数据


@app.route('/<name>')
def hello_name(name):
    return "Hello %s" %name

@app.route('/test')
def test_url_for():
    #url_for是返回路径的方法
    print(url_for('index'))
    return "test page"

@app.route('/meishi')
def meishi():
    return render_template('meishi.html')

#错误处理函数
@app.errorhandler(404)
def error_404(e):
    return '404 Error',404


#实际内容，用于模板中变量的替换
_name = 'minu'
_movies = [
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


#创建数据库模型 （类） 一个表对应一个类的实例
    #模型类要声明继承 db.Model
    #每一个类属型（字段）都需要实例化（db.Column）
    #传入的参数为字段的类型，还有额外的参数可以进行其他的设置，如设置主键，索引index
class User(db.Model): #表名将会是user,自动生成小写处理
    id = db.Column(db.Integer, primary_key = True) #主键
    name = db.Column(db.String(20)) #表名


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)#主键
    title = db.Column(db.String(60)) #电影标题
    year = db.Column(db.String(4)) #电影年份

#创建一个自定义命令来自动执行创建数据库表的操作
@app.cli.command() #注册为命令
@click.option('--drop', is_flag = True, help = 'Create after drop.') #设置首选项
def initdb(drop):
    if drop: #判断是否输入了选项
        db.drop_all()  #删除所有数据
    db.create_all() #创建表
    click.echo('Initialized databases.')

#把数据添加到数据库中
@app.cli.command()
def forge():
    """Generate fake data"""
    db.create_all()
    _name = 'minu'
    _movies = [
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
    user = User(name =_name)
    db.session.add(user)
    for i in _movies:
        movie = Movie(title = i['title'], year= i['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done!')




if __name__ == '__main__':
    app.debug = True
    app.run()


