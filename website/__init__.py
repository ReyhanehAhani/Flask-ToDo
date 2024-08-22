from flask import Flask

def creat_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'r147217287r'


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app


