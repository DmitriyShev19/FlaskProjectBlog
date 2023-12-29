from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jsdfhjsdhkjfk4212hsdfhlkjs'

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', title='Домашняя страница')


if __name__ == '__main__':
    app.run()
