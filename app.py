from flask import Flask

from views.hotties import bp as hotties_bp
from views.index import bp as index_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(hotties_bp)
