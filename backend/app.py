from flask import Flask, render_template, request, jsonify
import os

# prediction functions
from utils.text_predict import predict_text
from utils.image_predict import predict_image
from utils.voice_predict import predict_voice


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/text")
def text_page():
    return render_template("text.html")


@app.route("/image")
def image_page():
    return render_template("image.html")


@app.route("/voice")
def voice_page():
    return render_template("voice.html")


# -----------------------------
# TEXT DETECTION
# -----------------------------
@app.route("/predict_text", methods=["POST"])
def text_detection():

    text = request.form["text"]

    prediction, confidence = predict_text(text)

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence
    )


# -----------------------------
# IMAGE DETECTION
# -----------------------------
@app.route("/predict_image", methods=["POST"])
def image_detection():

    file = request.files["image"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    prediction, confidence = predict_image(filepath)

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence
    )


# -----------------------------
# VOICE DETECTION
# -----------------------------
@app.route("/predict_voice", methods=["POST"])
def voice_detection():

    file = request.files["audio"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    prediction, confidence = predict_voice(filepath)

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence
    )


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":

    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    app.run(debug=True)