from flask import Flask

def createApp(test_config=None):

    # name of the module that is currently running the app
    app = Flask(__name__)
    app.secret_key = 'efkjnvbhlewrbn874y845y4iefldm'
    # print(__name__)

    from . import UrlShort
    app.register_blueprint(UrlShort.bp)

    return app
