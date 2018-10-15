from flask_migrate import Migrate

from App.models import db


def init_ext(app):
    app.config['SECRET_KEY'] = '110'
    db.init_app(app=app)
    migrate = Migrate()
    migrate.init_app(app=app,db=db)