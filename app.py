#!/usr/local/bin/python3.7
try:
    import mimetypes
    mimetypes.init()
except Exception as e:
    pass

from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')