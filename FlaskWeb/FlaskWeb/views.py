from datetime import datetime
from flask import render_template
from FlaskWeb import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Главная',
        year=datetime.now().year,
        w1='Добро пожаловать!',
        w2='',
        w3='Состояние ячеек хранения',
        w4='Информацию о нашей команде вы можете найти ',
        w5='здесь',
        w6='Информация о пользователях',
    )


@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='Аренда ячеек',
        year=datetime.now().year,
        a1='Состояние:',
        ap1='Свободно',
        ap2='Занято',
        ac1='Ячейка хранения №1(маленькая)',
        ac2='Ячейка хранения №2(маленькая)',
        ac3='Ячейка хранения №3(большая)',
        ax='Подробнее',
    )


@app.route('/info')
def info():
    return render_template(
        'info.html',
        title='Информация',
        year=datetime.now().year,
        i1='Сайт был создан командой "Диаметр":',
        ix1='- Сергей Николаев(капитан)',
        ix2='- Алексей Бондаренко',
        ix3='- Кирилл Колмыков',
        ix4='- Анастасия Миронова',
        ix5='- Кирилл Кудряшов',
        i3='Наша документация',
        i4='ТутДолжнаБытьСсылка',
    )


@app.route('/userinfo')
def userinfo():
    return render_template(
        'userinfo.html',
        title='Информация о пользователях',
        year=datetime.now().year,
        iu1='Список пользователей:',
        iu2='Имя пользователя: ',
        iu3='RFID: ',
        iu4='Подробнее',
    )

@app.route('/usertest')
def usertest():
    return render_template(
        'usertest.html',
        title='Информация о пользователях',
        year=datetime.now().year,
        iu1='Информация о пользователе ',
        iu3='RFID: ',
        iu4='Аренды пользователя:',
        iu2='Назад',
        iu5='Время начала аренды: ',
        iu6='Время конца аренды: ',
        num='Номер ячейки: ',
        num1='№1(маленькая)',
        num2='№2(маленькая)',
        num3='№3(большая)',
    )

@app.route('/usertest1')
def usertest1():
    return render_template(
        'usertest1.html',
        title='Информация о пользователях',
        year=datetime.now().year,
        iu1='Информация о пользователе ',
        iu3='RFID: ',
        iu4='Аренды пользователя:',
        iu2='Назад',
        iu5='Время начала аренды: ',
        iu6='Время конца аренды: ',
                num='Номер ячейки: ',
        num1='№1(маленькая)',
        num2='№2(маленькая)',
        num3='№3(большая)',
    )


@app.route('/cell1')
def cell1():
    return render_template(
        'cell1.html',
        title='Аренда ячеек',
        year=datetime.now().year,
                ap1='Свободно',
        ap2='Занято',
        tm='10:00',
        rfi='17651467',
        nik='user#01',
        clr='',
    )


@app.route('/cell2')
def cell2():
    return render_template(
        'cell2.html',
        title='Аренда ячеек',
        year=datetime.now().year,
                ap1='Свободно',
        ap2='Занято',
        tm='',
        rfi='',
        nik='',
        clr='Готово к работе',
    )


@app.route('/cell3')
def cell3():
    return render_template(
        'cell3.html',
       title='Аренда ячеек',
        year=datetime.now().year,
                ap1='Свободно',
        ap2='Занято',
        tm='',
        rfi='',
        nik='',
        clr='Готово к работе',
    )





