from flask import Flask, url_for, request, render_template, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', Title='Главная')


@app.route('/training/<prof>')
def traning(prof):
    return render_template('training.html', prof=prof.lower())


@app.route('/list_prof/<mark>')
def list_prof(mark):
    li_prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
               'инженер по терраформированию', 'климатолог',
               'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
               'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
               'штурман', 'пилот дронов']
    return render_template('list_prof.html', mark=mark, list_prof=li_prof)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.file)
        f = form.file.data
        print(f)
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
