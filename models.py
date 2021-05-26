from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW

class Playlist(db.Model):
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)


class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

class PlaylistSong(db.Model):
    __tablename__ = "playlist_songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id', ondelete="cascade"))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id', ondelete="cascade"))

    song = db.relationship('Song', backref="playlist_songs", cascade="all, delete")
    playlist = db.relationship('Playlist', backref="playlist_songs", cascade="all, delete")
