# coding: utf-8
from flask import Flask, render_template
from redis import Redis
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/view/')
def hello():
    return render_template('view.html', content=redis.get('content'))

@app.route('/edit/<content>')
def edit(content=None):
    redis.set("content",content)
    return 'edit finish!'

#@app.route('/')
#def hello():
#    redis.incr('hits')
#    return 'aaaaa Hello World! I have been seen %s times.' % redis.get('hits')

#@app.route('/wao')
#def wao():
#    return 'wao'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

