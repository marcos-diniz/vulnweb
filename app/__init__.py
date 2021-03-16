from flask import Flask, request, redirect, current_app, render_template, session

def create_app():
  app = Flask(__name__)

  @app.route('/')
  @app.route('/index')
  def index():
    return "index page"

  @app.route('/login', methods=["GET", "POST"])
  def login():
    return "profile page"

  @app.route('/profile', methods=["GET"])
  def profile():
    return "profile page"

  @app.route('/signup', methods=["POST", "GET"])
  def signup():
    return "signup page"

  return app
