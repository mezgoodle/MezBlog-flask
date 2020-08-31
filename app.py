from config import Configuration
from posts.blueprint import posts

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(posts, url_prefix='/blog')

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import *
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))

@app.route('/')
@app.route('/index')
def index():
    name = 'mezgoodle'
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
