from flask import Flask, render_template, request, session, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Playlist, PlaylistSong, Song
from forms import AddPlaylistForm, AddSongForm, AddSongToPlaylist

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'crowBottom'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


connect_db(app)

@app.route('/')
def homepage():
    # homepage shows all playlists by default
    playlists = Playlist.query.all()
    return render_template('home.html', playlists=playlists)

# PLAYLIST ROUTES---------------------------------------------------------------
@app.route('/add_playlist', methods=["GET", "POST"])
def add_show_playlists():
    # add a playlist and view playlist songs
    form = AddPlaylistForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        new_playlist = Playlist(name=name,description=description)
        db.session.add(new_playlist)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("playlist_add_form.html", form=form)

@app.route('/playlist_detail/<int:id>')
def playlist_details(id):
    # show playlist details including song list
    id = id
    playlist = Playlist.query.get_or_404(id)
    playlist_songs = PlaylistSong.query.all()
    return render_template('playlist_detail.html', playlist=playlist, playlist_songs=playlist_songs, id=id)

@app.route("/playlist/<int:id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(id):

    playlist = Playlist.query.get_or_404(id)
    form = AddSongToPlaylist()
    form.song.choices = [(song.id, song.title) for song in Song.query.all()]
    song_id = form.song.data
    if form.validate_on_submit():
        playlist_song = PlaylistSong(playlist_id=id, song_id=song_id)
        db.session.add(playlist_song)
        db.session.commit()
        return redirect(f"/playlist_detail/{id}")

    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)


# SONG ROUTES-------------------------------------------------------------------
@app.route('/songs')
def add_show_songs():
    # add a playlist and view playlist songs
        all_songs = Song.query.all()
        return render_template("all_songs.html", all_songs=all_songs)

@app.route('/song_detail/<int:song_id>')
def song_details(song_id):
    song = Song.query.get_or_404(song_id)
    return render_template('song_details.html', song=song)

@app.route('/add_song', methods=["GET", "POST"])
def add_song():
    # add a playlist and view playlist songs
    form = AddSongForm()

    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data
        new_song = Song(title=title,artist=artist)
        db.session.add(new_song)
        db.session.commit()

        return redirect("/songs")

    else:
        return render_template("add_song_form.html", form=form)
