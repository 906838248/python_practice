# 让电脑支持服务访问，需要一个web框架
from flask import Flask, render_template, request, redirect, url_for
from random import choice

app = Flask(__name__)

people = [
    '张三',
    '李四',
    '王五'
]

@app.route('/')
def index():
    return render_template('index_pro.html', people=people)

@app.route('/input', methods=['GET', 'POST'])
def input_people():
    if request.method == 'POST':
        input_text = request.form.get('people_list')
        if input_text:
            people_list = [p.strip() for p in input_text.split('\n') if p.strip()]
            return render_template('index_pro.html', people=people_list)
    return render_template('input.html')

@app.route('/lottery')
def lottery():
    people_list = request.args.get('people')
    if people_list:
        people_list = people_list.split(',')
    else:
        people_list = people
    winner = choice(people_list)
    return render_template('index_pro.html', people=people_list, winner=winner)

if __name__ == '__main__':
    app.run(debug=True)