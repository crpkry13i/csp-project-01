import os
import re
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
# from sqlalchemy.exc import IntegrityError
import tekore as tk
import asyncio
from models import db, connect_db, User
from secret import client_id, client_secret
from forms import RegisterForm, LoginForm


app = Flask(__name__)

uri = os.getenv('DATABASE_URL')  # or other relevant config var
if uri and uri.startswith('postgres://'):
    uri = uri.replace('postgres://', 'postgresql://', 1)
# rest of connection code using the connection string `uri`

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///users_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secretbackup')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


BASE_API = "https://api.spotify.com"
AUTH = "https://accounts.spotify.com/authorize"
MY_URI = "spotify:artist:1wAkNf5IFauLqZgJFY2mAg"

client_id = client_id
client_secret = client_secret
redirect_uri = "http://127.0.0.1:5000"

# Retrieving a client token
app_token = tk.request_client_token(client_id, client_secret)

# Calling the API
spotify = tk.Spotify(app_token, sender=tk.AsyncSender())

# Artist ID
ryleinathaniel = "1wAkNf5IFauLqZgJFY2mAg"


async def get_artist_albums():
    return await spotify.artist_albums(ryleinathaniel, limit=50)

albums = asyncio.run(get_artist_albums())


connect_db(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """Handle user registation.
    Create new user and add to DB. Redirect to Music Page.
    If form not valid, present form.
    If there's already a user with that username: flash message and re-present form.
    """

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.register(username, password)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id

        flash(f"Welcome, {user.username}!")
        return redirect("/ryleinathaniel")
    else:
        flash("Username already taken, please try again.")
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in user."""

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # authenticate will return a user or False
        user = User.authenticate(username, password)

        if user:
            flash(f"Welcome, {user.username}!")
            session["user_id"] = user.id  # keep user logged in
            return redirect("/ryleinathaniel")
        else:
            form.username.errors = ["Incorrect username or password"]
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    """Log user out."""

    session.pop("user_id")
    return redirect("/")


@app.route('/ryleinathaniel')
def ryleinathaniel():
    if "user_id" not in session:
        flash("You must be logged in first")
        return redirect("/login")
    if (request.args.get('page')):
        page = int(request.args.get('page'))
    else:
        page = 1
    if (page == 1):
        album = albums.items[0]
        album2 = albums.items[1]
        album3 = albums.items[2]
        album4 = albums.items[3]
    if (page == 2):
        album = albums.items[4]
        album2 = albums.items[5]
        album3 = albums.items[6]
        album4 = albums.items[7]
    if (page == 3):
        album = albums.items[8]
        album2 = albums.items[9]
        album3 = albums.items[10]
        album4 = albums.items[11]
    if (page == 4):
        album = albums.items[12]
        album2 = albums.items[13]
        album3 = albums.items[14]
        album4 = albums.items[15]
    if (page == 5):
        album = albums.items[16]
        album2 = albums.items[17]
        album3 = albums.items[18]
        album4 = albums.items[19]
    if (page == 6):
        album = albums.items[20]
        album2 = albums.items[21]
        album3 = albums.items[22]
        album4 = albums.items[23]
    if (page == 7):
        album = albums.items[24]
        album2 = albums.items[25]
        album3 = albums.items[26]
        album4 = albums.items[27]
    if (page == 8):
        album = albums.items[28]
        album2 = albums.items[29]
        album3 = albums.items[30]
        album4 = albums.items[31]
    return render_template('base-ryleinathaniel.html', album=album, album2=album2, album3=album3, album4=album4, page=page)

###############################################################################################################

    # album_image = albums.items[0].images[1].url
    # album_image1 = albums.items[1].images[1].url
    # album_image2 = albums.items[2].images[1].url
    # album_image3 = albums.items[3].images[1].url
    # album_name = albums.items[0].name
    # album_name1 = albums.items[1].name
    # album_name2 = albums.items[2].name
    # album_name3 = albums.items[3].name
    # release_date = albums.items[0].release_date
    # release_date1 = albums.items[1].release_date
    # release_date2 = albums.items[2].release_date
    # release_date3 = albums.items[3].release_date
    # album_link = albums.items[0].external_urls['spotify']
    # album_link1 = albums.items[1].external_urls['spotify']
    # album_link2 = albums.items[2].external_urls['spotify']
    # album_link3 = albums.items[3].external_urls['spotify']
    # return render_template('01.html',
    #                        album_image=album_image,
    #                        album_image1=album_image1,
    #                        album_image2=album_image2,
    #                        album_image3=album_image3,
    #                        album_name=album_name,
    #                        album_name1=album_name1,
    #                        album_name2=album_name2,
    #                        album_name3=album_name3,
    #                        release_date=release_date,
    #                        release_date1=release_date1,
    #                        release_date2=release_date2,
    #                        release_date3=release_date3,
    #                        album_link=album_link,
    #                        album_link1=album_link1,
    #                        album_link2=album_link2,
    #                        album_link3=album_link3)


# @ app.route('/2')
# def second_page():
#     album_image = albums.items[4].images[1].url
#     album_image1 = albums.items[5].images[1].url
#     album_image2 = albums.items[6].images[1].url
#     album_image3 = albums.items[7].images[1].url
#     album_name = albums.items[4].name
#     album_name1 = albums.items[5].name
#     album_name2 = albums.items[6].name
#     album_name3 = albums.items[7].name
#     release_date = albums.items[4].release_date
#     release_date1 = albums.items[5].release_date
#     release_date2 = albums.items[6].release_date
#     release_date3 = albums.items[7].release_date
#     album_link = albums.items[4].external_urls['spotify']
#     album_link1 = albums.items[5].external_urls['spotify']
#     album_link2 = albums.items[6].external_urls['spotify']
#     album_link3 = albums.items[7].external_urls['spotify']
#     return render_template('02.html',
#                            album_image=album_image,
#                            album_image1=album_image1,
#                            album_image2=album_image2,
#                            album_image3=album_image3,
#                            album_name=album_name,
#                            album_name1=album_name1,
#                            album_name2=album_name2,
#                            album_name3=album_name3,
#                            release_date=release_date,
#                            release_date1=release_date1,
#                            release_date2=release_date2,
#                            release_date3=release_date3,
#                            album_link=album_link,
#                            album_link1=album_link1,
#                            album_link2=album_link2,
#                            album_link3=album_link3)


# @ app.route('/3')
# def third_page():
#     album_image = albums.items[8].images[1].url
#     album_image1 = albums.items[9].images[1].url
#     album_image2 = albums.items[10].images[1].url
#     album_image3 = albums.items[11].images[1].url
#     album_name = albums.items[8].name
#     album_name1 = albums.items[9].name
#     album_name2 = albums.items[10].name
#     album_name3 = albums.items[11].name
#     release_date = albums.items[8].release_date
#     release_date1 = albums.items[9].release_date
#     release_date2 = albums.items[10].release_date
#     release_date3 = albums.items[11].release_date
#     album_link = albums.items[8].external_urls['spotify']
#     album_link1 = albums.items[9].external_urls['spotify']
#     album_link2 = albums.items[10].external_urls['spotify']
#     album_link3 = albums.items[11].external_urls['spotify']
#     return render_template('03.html',
#                            album_image=album_image,
#                            album_image1=album_image1,
#                            album_image2=album_image2,
#                            album_image3=album_image3,
#                            album_name=album_name,
#                            album_name1=album_name1,
#                            album_name2=album_name2,
#                            album_name3=album_name3,
#                            release_date=release_date,
#                            release_date1=release_date1,
#                            release_date2=release_date2,
#                            release_date3=release_date3,
#                            album_link=album_link,
#                            album_link1=album_link1,
#                            album_link2=album_link2,
#                            album_link3=album_link3)


# @ app.route('/4')
# def fourth_page():
#     album_image = albums.items[12].images[1].url
#     album_image1 = albums.items[13].images[1].url
#     album_image2 = albums.items[14].images[1].url
#     album_image3 = albums.items[15].images[1].url
#     album_name = albums.items[12].name
#     album_name1 = albums.items[13].name
#     album_name2 = albums.items[14].name
#     album_name3 = albums.items[15].name
#     release_date = albums.items[12].release_date
#     release_date1 = albums.items[13].release_date
#     release_date2 = albums.items[14].release_date
#     release_date3 = albums.items[15].release_date
#     album_link = albums.items[12].external_urls['spotify']
#     album_link1 = albums.items[13].external_urls['spotify']
#     album_link2 = albums.items[14].external_urls['spotify']
#     album_link3 = albums.items[15].external_urls['spotify']
#     return render_template('04.html',
#                            album_image=album_image,
#                            album_image1=album_image1,
#                            album_image2=album_image2,
#                            album_image3=album_image3,
#                            album_name=album_name,
#                            album_name1=album_name1,
#                            album_name2=album_name2,
#                            album_name3=album_name3,
#                            release_date=release_date,
#                            release_date1=release_date1,
#                            release_date2=release_date2,
#                            release_date3=release_date3,
#                            album_link=album_link,
#                            album_link1=album_link1,
#                            album_link2=album_link2,
#                            album_link3=album_link3)


# @ app.route('/5')
# def fifth_page():
#     album_image = albums.items[16].images[1].url
#     album_image1 = albums.items[17].images[1].url
#     album_image2 = albums.items[18].images[1].url
#     album_image3 = albums.items[19].images[1].url
#     album_name = albums.items[16].name
#     album_name1 = albums.items[17].name
#     album_name2 = albums.items[18].name
#     album_name3 = albums.items[19].name
#     release_date = albums.items[16].release_date
#     release_date1 = albums.items[17].release_date
#     release_date2 = albums.items[18].release_date
#     release_date3 = albums.items[19].release_date
#     album_link = albums.items[16].external_urls['spotify']
#     album_link1 = albums.items[17].external_urls['spotify']
#     album_link2 = albums.items[18].external_urls['spotify']
#     album_link3 = albums.items[19].external_urls['spotify']
#     return render_template('05.html',
#                            album_image=album_image,
#                            album_image1=album_image1,
#                            album_image2=album_image2,
#                            album_image3=album_image3,
#                            album_name=album_name,
#                            album_name1=album_name1,
#                            album_name2=album_name2,
#                            album_name3=album_name3,
#                            release_date=release_date,
#                            release_date1=release_date1,
#                            release_date2=release_date2,
#                            release_date3=release_date3,
#                            album_link=album_link,
#                            album_link1=album_link1,
#                            album_link2=album_link2,
#                            album_link3=album_link3)


# @ app.route('/6')
# def sixth_page():
#     album_image = albums.items[20].images[1].url
#     album_image1 = albums.items[21].images[1].url
#     album_image2 = albums.items[22].images[1].url
#     album_image3 = albums.items[23].images[1].url
#     album_name = albums.items[20].name
#     album_name1 = albums.items[21].name
#     album_name2 = albums.items[22].name
#     album_name3 = albums.items[23].name
#     release_date = albums.items[20].release_date
#     release_date1 = albums.items[21].release_date
#     release_date2 = albums.items[22].release_date
#     release_date3 = albums.items[23].release_date
#     album_link = albums.items[20].external_urls['spotify']
#     album_link1 = albums.items[21].external_urls['spotify']
#     album_link2 = albums.items[22].external_urls['spotify']
#     album_link3 = albums.items[23].external_urls['spotify']
#     return render_template('06.html',
#                            album_image=album_image,
#                            album_image1=album_image1,
#                            album_image2=album_image2,
#                            album_image3=album_image3,
#                            album_name=album_name,
#                            album_name1=album_name1,
#                            album_name2=album_name2,
#                            album_name3=album_name3,
#                            release_date=release_date,
#                            release_date1=release_date1,
#                            release_date2=release_date2,
#                            release_date3=release_date3,
#                            album_link=album_link,
#                            album_link1=album_link1,
#                            album_link2=album_link2,
#                            album_link3=album_link3)


# @ app.route('/7')
# def seventh_page():
#     album_image = albums.items[24].images[1].url
#     album_image1 = albums.items[25].images[1].url
#     album_image2 = albums.items[26].images[1].url
#     album_image3 = albums.items[27].images[1].url
#     album_name = albums.items[24].name
#     album_name1 = albums.items[25].name
#     album_name2 = albums.items[26].name
#     album_name3 = albums.items[27].name
#     release_date = albums.items[24].release_date
#     release_date1 = albums.items[25].release_date
#     release_date2 = albums.items[26].release_date
#     release_date3 = albums.items[27].release_date
#     album_link = albums.items[24].external_urls['spotify']
#     album_link1 = albums.items[25].external_urls['spotify']
#     album_link2 = albums.items[26].external_urls['spotify']
#     album_link3 = albums.items[27].external_urls['spotify']
#     return render_template('07.html',
#                            album_image=album_image,
#                            album_image1=album_image1,
#                            album_image2=album_image2,
#                            album_image3=album_image3,
#                            album_name=album_name,
#                            album_name1=album_name1,
#                            album_name2=album_name2,
#                            album_name3=album_name3,
#                            release_date=release_date,
#                            release_date1=release_date1,
#                            release_date2=release_date2,
#                            release_date3=release_date3,
#                            album_link=album_link,
#                            album_link1=album_link1,
#                            album_link2=album_link2,
#                            album_link3=album_link3)


# @ app.route('/8')
# def eighth_page():
#     album_image = albums.items[28].images[1].url
#     album_image1 = albums.items[29].images[1].url
#     album_image2 = albums.items[30].images[1].url
#     album_image3 = albums.items[31].images[1].url
#     album_name = albums.items[28].name
#     album_name1 = albums.items[29].name
#     album_name2 = albums.items[30].name
#     album_name3 = albums.items[31].name
#     release_date = albums.items[28].release_date
#     release_date1 = albums.items[29].release_date
#     release_date2 = albums.items[30].release_date
#     release_date3 = albums.items[31].release_date
#     album_link = albums.items[28].external_urls['spotify']
#     album_link1 = albums.items[29].external_urls['spotify']
#     album_link2 = albums.items[30].external_urls['spotify']
#     album_link3 = albums.items[31].external_urls['spotify']
#     return render_template('08.html',
#                            album_image=album_image,
#                            album_image1=album_image1,
#                            album_image2=album_image2,
#                            album_image3=album_image3,
#                            album_name=album_name,
#                            album_name1=album_name1,
#                            album_name2=album_name2,
#                            album_name3=album_name3,
#                            release_date=release_date,
#                            release_date1=release_date1,
#                            release_date2=release_date2,
#                            release_date3=release_date3,
#                            album_link=album_link,
#                            album_link1=album_link1,
#                            album_link2=album_link2,
#                            album_link3=album_link3
#                            )
