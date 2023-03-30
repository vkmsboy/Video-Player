# Coded by Noob, so don't laugh.
# Make pull request if you found something wrong
# (c) Jigar Varma (Jigarvarma2005)
# Kangers copy with credits

import os
import requests
from urllib.parse import unquote_plus
from flask import Flask, jsonify, request
from flask import render_template
from youtube_dl import YoutubeDL
from base64 import standard_b64encode, standard_b64decode

app = Flask(__name__)

__author__ = "Jigarvarma2005"

ACCOUNT_ID = os.environ.get("ACCOUNT_ID", "6206459123001")
BCOV_POLICY = os.environ.get("BCOV_POLICY", "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd")

def str_to_b64(__str: str) -> str:
    str_bytes = __str.encode('ascii')
    bytes_b64 = standard_b64encode(str_bytes)
    b64 = bytes_b64.decode('ascii')
    return b64


def b64_to_str(b64: str) -> str:
    bytes_b64 = b64.encode('ascii')
    bytes_str = standard_b64decode(bytes_b64)
    __str = bytes_str.decode('ascii')
    return __str

@app.route("/")
def homepage():
    return render_template("index1.html")

if __name__ == "__main__":
    app.run(debug=True)

