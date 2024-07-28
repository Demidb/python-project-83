from flask import Flask
app = Flask(__name__)

import os
from dotenv import load_dotenv

@app.route('/')
def index() -> str:
    return ('index.html')


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')