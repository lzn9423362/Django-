from flask import render_template
from flask_script import Manager
from App import init_app

app = init_app()
manager = Manager(app)

@app.route('/')
def hello_world():
    return render_template('response.html', name='男人')


if __name__ == '__main__':
     app.run(debug=True,host='0')
