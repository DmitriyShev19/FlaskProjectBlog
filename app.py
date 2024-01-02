from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jsdfhjsdhkjfk4212hsdfhlkjs'


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', title='Домашняя страница')


@app.route('/where_to_begin')
def where_to_begin():
    return render_template('where_to_begin.html', title='С чего начать?')

@app.route('/folk')
def folk():
    return render_template('folk.html', title='Фолклер')


if __name__ == '__main__':
    app.run(debug=True)
