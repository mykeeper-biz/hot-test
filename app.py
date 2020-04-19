from flask import Flask
from views.index import bp as index_bp
from views.exercise_1 import bp as exercise_1_bp
from views.exercise_2 import bp as exercise_2_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(exercise_1_bp)
app.register_blueprint(exercise_2_bp)
