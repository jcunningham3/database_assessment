from models import Playlist, PlaylistSong, Song, db
from app import app

db.drop_all()
db.create_all()

# create table playlists
p1 = Playlist(name="Best of the Doors", description="Summer Playlist")
p2 = Playlist(name="Chill Mix", description="Just Trying To Post")

# create table songs
s1 = Song(title="Rider's on the Storm", artist="The Doors")
s2 = Song(title="When The Music's Over", artist="The Doors")
s3 = Song(title="Light My fire", artist="The Doors")
s4 = Song(title="L.A. Woman", artist="The Doors")
s5 = Song(title="Redemption Song", artist="Bob Marley")
s6 = Song(title="Diamonds On The Soles Of Her Shoes", artist="Paul Simon")
s7 = Song(title="Red House", artist="Jimi Henfdrix")
s8 = Song(title="Wigwam", artist="Bob Dylan")

# create table with songs on playlists
p1s1 = PlaylistSong(playlist_id=1, song_id=1)
p1s2 = PlaylistSong(playlist_id=1, song_id=2)
p1s3 = PlaylistSong(playlist_id=1, song_id=3)
p1s4 = PlaylistSong(playlist_id=1, song_id=4)

p2s1 = PlaylistSong(playlist_id=2, song_id=5)
p2s2 = PlaylistSong(playlist_id=2, song_id=6)
p2s3 = PlaylistSong(playlist_id=2, song_id=7)
p2s4 = PlaylistSong(playlist_id=2, song_id=8)

# add everything to the session
db.session.add(p1)
db.session.add(p2)

db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(s4)
db.session.add(s5)
db.session.add(s6)
db.session.add(s7)
db.session.add(s8)

db.session.add(p1s1)
db.session.add(p1s2)
db.session.add(p1s3)
db.session.add(p1s4)
db.session.add(p2s1)
db.session.add(p2s2)
db.session.add(p2s3)
db.session.add(p2s4)

# commit adds
db.session.commit()
