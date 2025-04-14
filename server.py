from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def s():
    return render_template('index.html', title='M')


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


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def res(nickname, level, rating):
    s = f'''
    <html>
    <head>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" />
    <title>Варианты выбора</title>
    <h1>Результаты отбора</h1>
    <h2>Претендент на участие в миссии: {nickname}</h2>
    <p><div class="p-3 mb-2 bg-primary text-white"> Поздравляем! Ваш рейтинг после {level} этапа отбора:;</div>
    <h3>Составляет {rating}!</h3>
    <p><div class="p-3 mb-2 bg-secondary text-white">Желаем удачи!;</div>
    </head>
    </html> 
    '''
    return s


@app.route('/landscape')
def landscape():
    s = f'''
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Пейзажи Марса</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" />
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
        <style>
        .carousel-container {{
                width: 800px;
                margin: 50px auto;}}
        </style>
    </head>
    <body class="bg-light">
        <div class="container text-center mt-5">
            <h1 class="mb-4">Пейзажи Марса</h1>
        </div>

        <div class="carousel-container">
            <div id="carouselExampleControlsNoTouching" class="carousel slide" data-bs-touch="false">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="/static/img/mars1.jpg" class="d-block w-100 rounded" alt="Mars 1">
                    </div>
                    <div class="carousel-item">
                        <img src="/static/img/mars2.jpg" class="d-block w-100 rounded" alt="Mars 2">
                    </div>
                    <div class="carousel-item">
                        <img src="/static/img/mars3.jpg" class="d-block w-100 rounded" alt="Mars 3">
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Предыдущий</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Следующий</span>
                </button>
            </div>
        </div>
    </body>
    </html>
    '''
    return s


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        return render_template('train.html', title2='Инженерные тренажеры')
    return render_template('train.html', title2='Научные симуляторы')


lst_profess = [
    "инженер-исследователь",
    "пилот",
    "строитель",
    "экзобиолог",
    "врач",
    "инженер по терраформированию",
    "климатолог",
    "специалист по радиационной защите",
    "астрогеолог",
    "гляциолог",
    "инженер жизнеобеспечения",
    "метеоролог",
    "оператор марсохода",
    "киберинженер",
    "штурман",
    "пилот дронов"
]


@app.route('/list_prof/<num>')
def list_prof(num):
    return render_template('list_prof.html', list_prof=lst_profess, op=num)


@app.route('/distribution')
def distribution():
    astronauts = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венката Капур",
        "Тедди Сандерс",
        "Шон Бин"
    ]
    return render_template("distribution.html", astronauts=astronauts)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        man = dict()
        man['email'] = request.form.get('email')
        man['about'] = request.form.get('about')
        man['scholl_class'] = request.form.get('class')
        return render_template('auto_answer.html', **man)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
