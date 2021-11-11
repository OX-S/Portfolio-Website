import pandas as pd
import os
from github import Github
from flask import Blueprint, render_template, url_for, redirect, request
from forms import ContactForm


views = Blueprint(__name__, "views")
links = [("ArcticDevelopment", "ArcticTools"),
         ("OX-S", "Discord-Custom-Status-Changer"),
         ('OX-S', 'Python-Mandelbrot'),
         ('ArcticDevelopment', 'ArcticDarkzone')]


@views.route("/")
def landing():
    return redirect(url_for('views.home'))


@views.route("/home")
def home():
    return render_template("home.html")


@views.route("/photography")
def photog():
    return render_template("photog.html")


@views.route("/github")
def github():
    repo_list = []
    for link in links:
        r = Github.get_repo(link[0], link[1])
        t = (f'https://www.github.com/{link[0]}/{link[1]}',
             Github.get_name(r),
             Github.get_desc(r),
             Github.get_forks(r),
             Github.get_stars(r),
             Github.get_language(r)
             )
        repo_list.append(t)
    return render_template("github.html", data=repo_list)


@views.route("/artwork")
def artwork():
    return render_template("artwork.html")


@views.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        try:
            response = pd.DataFrame([[name, email, message]])
            response.to_csv('data.csv', mode='a', header=False)

        except FileNotFoundError:

            df = pd.DataFrame([[name, email, message]], columns=['a', 'b', 'c'])
            df.to_csv('data.csv')

        print("The data is saved !")
        return render_template('contact.html', form=form)
    else:
        return render_template('contact.html', form=form)
