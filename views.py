import pandas as pd
import os

from github import Github
from flask import Blueprint, render_template, url_for, redirect, request, send_file
from forms import ContactForm
from photo import *
from math import floor
from artwork import *

views = Blueprint(__name__, "views")
links = [("ArcticDevelopment", "ArcticTools"),
         ("OX-S", "Discord-Custom-Status-Changer"),
         ('OX-S', 'Python-Mandelbrot'),
         ('ArcticDevelopment', 'ArcticDarkzone'),
         ('OX-S', 'Portfolio-Website')]


@views.route("/")
def landing():
    return redirect(url_for('views.home'))


@views.route("/home")
def home():
    return render_template("home.html")


@views.route("/photography")
def photog():
    photos = []
    path = os.path.join(os.getcwd(), 'static/assets/photographs/')

    files = [os.path.join(path, f) for f in os.listdir(path)
             if os.path.isfile(os.path.join(path, f))]
    for file in files:
        name = Photo.get_name(file)
        exif = Photo.get_exif(file)
        device = Photo.get_device(exif)
        ss = Photo.get_shutter_speed(exif)
        f_stop = Photo.get_f_stop(exif)
        iso = Photo.get_iso(exif)
        focal_length = Photo.get_focal_length(exif)
        data = (file.replace(os.path.join(os.getcwd(), 'static/'), ''), name, device, ss, f_stop, iso, focal_length)
        photos.append(data)

    lists = [photos[x:x + (floor(len(photos) / 3)) + 1] for x in range(0, len(photos), floor(len(photos) / 3) + 1)]
    return render_template("photog.html", data=lists)


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
    artworks = []

    files = [f for f in os.listdir('static/assets/artwork/')
             if os.path.isfile(os.path.join('static/assets/artwork/', f))]
    for file in files:
        art_piece = Artwork(file)
        print(art_piece.get_name())
        print(art_piece.get_median())
        print(art_piece.get_path())
        artworks.append(art_piece.get_list())
    return render_template("artwork.html", data=artworks)


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

            df = pd.DataFrame([[name, email, message]])
            df.to_csv('data.csv')

        return render_template('contact.html', form=form)
    else:
        return render_template('contact.html', form=form)


@views.route("/download")
def download_file():
    p = "Finn_Kliewer_Resume.pdf"
    return send_file(p, as_attachment=True)
