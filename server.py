from flask import Flask

app = Flask(__name__)


@app.route('/')
def s():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    text = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
    return '<html>' + '<br>'.join(text) + '</html>'


@app.route('/image_mars')
def image_mars():
    s = '''
    <html>
    <head>
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src = "/static/img/MARS.png">
    <p>Вот она какая, красная планета!</p>
    </head>
    </html> 
    '''
    return s


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
