from flask.helpers import url_for
from config import Configuration
from posts.blueprint import posts

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(posts, url_prefix='/blog')


@app.route('/')
@app.route('/index')
def index():
    name = 'mezgoodle'
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
