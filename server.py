from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def s():
    return render_template('index.html', user='e')


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
    s = f'''
    <html>
    <head>
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src = "/static/img/MARS.png">
    </head>
    </html> 
    '''
    return s


@app.route('/promotion_image')
def promotion_image():
    s = f'''
    <html>
    <head>
    
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" />
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src = "/static/img/MARS.png">
    <p><div class="p-3 mb-2 bg-primary text-white">Человечество вырастает из детства.</div>
    <div class="p-3 mb-2 bg-secondary text-white">Человечеству мала одна планета.</div>
    <div class="p-3 mb-2 bg-success text-white">Мы сделаем обитаемыми безжизненные пока планеты.</div>
    <div class="p-3 mb-2 bg-danger text-white">И начнем с Марса!</div>
    <div class="p-3 mb-2 bg-warning text-dark">Присоединяйся!</div></p>
    </head>
    </html> 
    '''
    return s


@app.route('/choice/<planet_name>')
def choice(planet_name):
    s = f'''
    <html>
    <head>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" />
    <title>Варианты выбора</title>
    <h1>Мое предложение: {planet_name}</h1>
    <h2>Эта планета близка к Земле</h2>
    <p><div class="p-3 mb-2 bg-primary text-white">На ней много полезных ресурсов;</div>
    <div class="p-3 mb-2 bg-secondary text-white">На ней есть вода и атмосфера;</div>
    <div class="p-3 mb-2 bg-success text-white">На ней есть небольшое магнитное поле;</div>
    <div class="p-3 mb-2 bg-danger text-white">Наконец, она просто красива!</div>
    </head>
    </html> 
    '''
    return s



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
