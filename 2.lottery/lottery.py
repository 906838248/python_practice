# 让电脑支持服务访问，需要一个web框架
from flask import Flask, render_template
from random import randint

app = Flask(__name__)

people = [
    '张三',
    '李四',
    '王五'
]

@app.route('/index')
def index():
    return render_template('index.html', people=people)

@app.route('/lottery')
def lottery():
    # randint 随机生成一个整数, 包括左右端点
    num = randint(0, len(people)-1)
    winner = people[num]
    return render_template('index.html', winner=winner, people=people)
app.run(debug=True)