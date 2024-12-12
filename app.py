from flask import Flask, render_template, request, redirect, url_for, flash
import cv2
import numpy as np
import base64
from deepface import DeepFace
import json

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

def decode_image(data_uri):
    header, encoded = data_uri.split(",", 1)
    data = base64.b64decode(encoded)
    np_array = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return image

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    file_in = open('static/login_info.json', 'r')
    users = json.load(file_in)
    file_in.close()

    username = request.form['username']
    password = request.form['password']
    image_data = request.form.get('image_data')

    if username in users and users[username]['password'] == password:
        try:
            captured_image = decode_image(image_data)
            result = DeepFace.verify(captured_image,
                                     users[username]['face_encoding'],
                                     model_name='Facenet',
                                     anti_spoofing=True)
            if result["verified"]:
                return redirect(url_for('home', username= username))
            else:
                flash("Face recognition failed. Please try again.")
        except ValueError as e:
            flash(f"No picture is taken. Please try again")
    else:
        flash("Invalid username or password.")

    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    file_in = open('static/login_info.json', 'r')
    users = json.load(file_in)
    file_in.close()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        image_data = request.form.get('image_data')

        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for('register'))

        if username in users:
            flash("Username already exists.")
            return redirect(url_for('register'))

        try:
            captured_image = decode_image(image_data)
            face_encoding = DeepFace.represent(captured_image,
                                               model_name='Facenet',
                                               anti_spoofing=True)[0]['embedding']

            image_path = f"static/verification_image/{username}.jpg"
            users[username] = {
                "username": username,
                "password": password,
                "image_path": image_path,
                "face_encoding": face_encoding
            }

            file_out = open('static/login_info.json', 'w')
            json.dump(users, file_out, indent= 4)

            cv2.imwrite(image_path, captured_image)

            flash("Registration successful. Please log in.")
            return redirect(url_for('index'))
        except ValueError as e:
            flash(f"No picture is taken. Please try again")
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
