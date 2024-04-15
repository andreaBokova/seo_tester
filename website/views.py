from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/keyword-explorer')
def keyword_explorer():
    return render_template("keyword-explorer.html")

