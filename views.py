from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/Profile")
def profile():
    return render_template("profile.html")

@views.route("/Portfolio")
def portfolio():
    return render_template("portfolio.html")

@views.route("/Skills")
def skills():
    return render_template("skills.html")

@views.route("/Bio")
def bio():
        return render_template("bio.html")


@views.route("/Vision")
def vision():
     return render_template("vision.html")

@views.route("/Education")
def education():
     return render_template("education.html")