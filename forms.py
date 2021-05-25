from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, Email

class AddPlaylistForm(FlaskForm):
    name = StringField("Playlist Name", validators=[InputRequired()])
    description = StringField("Playlist description", validators=[InputRequired()])

class AddSongForm(FlaskForm):
    title = StringField("Song Title")
    artist = StringField("Artist")

class AddSongToPlaylist(FlaskForm):
    song = SelectField(u"Songs")
