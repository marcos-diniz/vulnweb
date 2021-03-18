from flask import url_for, request, redirect, current_app, render_template, session
#from database import get_db

def configure(app):
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/signup', methods=["POST", "GET"])
    def signup():
        return render_template('signup.html')

    @app.route('/signin', methods=["GET", "POST"])
    def signin():
        if request.method == "GET":
            return render_template('signin.html')

        elif request.method == "POST":
            name = request.form.get('username')
            password = request.form.get('password')

            return redirect(url_for('app.profile'))

    @app.route('/profile', methods=["GET"])
    def profile():
       return render_template('profile.html')


    return app