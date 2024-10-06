from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from config import Config
from routes import overlay_routes, video_routes

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

app.register_blueprint(overlay_routes)
app.register_blueprint(video_routes)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)