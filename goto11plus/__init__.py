from flask import Flask
from goto11plus import pages 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    return app