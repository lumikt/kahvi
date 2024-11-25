from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

test_env = getenv("TEST_ENV") == "true"
print(f"Test environment: {test_env}")


app.secret_key = getenv("SECRET_KEY")
if test_env:
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("TEST_DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

db = SQLAlchemy(app)
