import numpy as np
import cv2
import joblib

# load both models
model1 = joblib.load(open("models/ai_text_detector_model.joblib", "rb"))
model2 = joblib.load(open("models/tfidf_vectorizer.joblib", "rb"))


def preprocess_image(image_path):

    img = cv2.imread(image_path)

    img = cv2.resize(img,(128,128))

    img = img.flatten()

    return img


def predict_image(image_path):

    img = preprocess_image(image_path)

    img = vectorizer.transform([img])

    prediction = model.predict(img)[0]

    confidence = model.predict_proba(img).max()

    if prediction == 1:
        label = "AI Generated Image"
    else:
        label = "Real Image"

    return label, round(confidence*100,2)