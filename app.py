from config import Configuration

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/')
@app.route('/index')
def index():
    name = 'mezgoodle'
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
