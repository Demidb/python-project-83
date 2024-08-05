from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)

import os
from dotenv import load_dotenv
import psycopg2
import requests
from .url import normalize_url, validate_url
from datetime import datetime


@app.route('/')
def index() -> str:
    return ('index.html')


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

@app.route('/urls', methods=['POST'])
def urls_post() -> str:
    url_from_request = request.form.to_dict().get('url', '')
    errors = validate_url(url_from_request)

    if 'Not valid url' in errors:
        flash('Некорректный URL', 'alert-danger')
        if 'No url' in errors:
            flash('URL обязателен', 'alert-danger')
        return render_template('index.html'), 422

    new_url = normalize_url(url_from_request)
