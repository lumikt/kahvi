
from config import app
from flask import redirect, render_template, request, jsonify, flash


@app.route("/", methods =["GET", "POST"])
def load_index():    
    return render_template("index.html")
