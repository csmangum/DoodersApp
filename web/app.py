from flask import request, Flask, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        print('oh yeah baby')
        
    else:
        return render_template('index.html')


@app.route('/plus_one')
def plus_one():
    x = int(request.args.get('x', 1))
    return json.dumps({'x': x + 1})


@app.route('/square')
def square():
    x = int(request.args.get('x', 1))
    return json.dumps({'x': x * x})
