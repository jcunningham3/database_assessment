from models import Playlist, PlaylistSong, Song, db
from app import app

db.drop_all()
db.create_all()

p1 = Playlist(name="Best of the Doors", description="Rainy Day Playlist")

s1 = Song(title="Rider's on the Storm", artist="The Doors")
s2 = Song(title="The Sky Is Crying", artist="Stevie Ray Vaughn")

p1s1 = PlaylistSong(playlist_id=1, song_id=1)
p1s2 = PlaylistSong(playlist_id=1, song_id=2)


db.session.add(p1)

db.session.add(s1)
db.session.add(s2)




db.session.commit()
