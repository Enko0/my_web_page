from flask import Flask, render_template, request, redirect, url_for, session, flash, Response
import hashlib
import pandas as pd
import sqlite3
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import os
import requests


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ne




@app.route("/pokemon", methods=["GET", "POST"])
def index():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)