import os
from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ["APP_SETTINGS"])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["UPLOAD_FOLDER"] = "/home/app/static/media"
    db.init_app(app)

    @app.route("/")
    def hello_world():
        return jsonify(hello="world")

    @app.route("/upload", methods=["POST"])
    def upload_image():
        if "file" not in request.files:
            return jsonify(error="no file"), 400
        file = request.files["file"]
        if file.filename == "":
            return jsonify(error="no filename"), 400
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return jsonify(file=filename)

    @app.route("/media/<filename>")
    def get_image(filename):
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

    return app
