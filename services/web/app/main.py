import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite://")
app.config["MEDIA_FOLDER"] = "/usr/src/app/mediafiles"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "no file"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "no filename"}), 400
    filename = secure_filename(file.filename)
    os.makedirs(app.config["MEDIA_FOLDER"], exist_ok=True)
    file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    return jsonify({"file": filename}), 201
