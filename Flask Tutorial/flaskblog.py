from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SECRET_KEY'] = "7a6e543cfceff24f54b5336eacf71eb8"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())
posts = [
    {
        "author": "Ben Kennedy",
        "title": "Post Numebr One",
        "content": "First Post Content",
        "date_posted": "April 20th 2022"
    },
    {
        "author": "Tom Hanks",
        "title": "Post Numebr Two",
        "content": "Second Post Content",
        "date_posted": "April 21st 2022"
    }
]

# decorator that runs function when we are at / or /home directory
@app.route("/")
@app.route("/home")
def home():
    # define template to return and pass 'posts' variable for template to use
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created For {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == "admin@admin.com" and form.password.data == "admin":
            flash("You are now logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login failed. Try again", "danger")
            
    
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)
    print(datetime.utcnow)