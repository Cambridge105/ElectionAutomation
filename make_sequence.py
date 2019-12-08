import os, random, glob, datetime

os.system ("rm /home/liquidsoap/radio/elex/sequence_MP3WRAP.mp3")
command = "mp3wrap /home/liquidsoap/radio/elex/sequence.mp3 "


# Get the list of all tracks
musicdir = '/home/liquidsoap/radio/elex/music'
list_of_music = glob.glob(musicdir + '/*.mp3')

# Get the list of all jingles
jinglesdir = '/home/liquidsoap/radio/elex/jingles'
list_of_jingles = glob.glob(jinglesdir + '/*.mp3')

# Get the list of playlist tracks
playlistdir = '/home/liquidsoap/radio/elex/playlist'
list_of_playlist = glob.glob(playlistdir + '/*.mp3')

# Set up the array which will hold the files to be sequenced
tracks = []

# If the next sequence starts at :00, play 2 mins silence, else play SNR
now = datetime.datetime.now()

# TODO: Add to the TOTH
if (now.minute < 45):
  tracks.append('/home/liquidsoap/radio/elex/snrnews-safe.mp3')
  # TODO: Replace with the half-past hour intro
  tracks.append('/home/liquidsoap/radio/elex/idents/toth.mp3')
else:
  tracks.append('/home/liquidsoap/radio/elex/idents/toth.mp3')

# Add a random track
rndTrack = random.choice(list_of_music)
tracks.append(rndTrack)

# Add the Cambridge package (will be blank if none)
tracks.append('/home/liquidsoap/radio/elex/cambridge_MP3WRAP.mp3')

# Add the S. Cambs package (will be blank if none)
tracks.append('/home/liquidsoap/radio/elex/s_cambs_MP3WRAP.mp3')

# Add link for SE Cambs if there are SE Cambs clips
seclipsdir = '/home/liquidsoap/radio/elex/clips_safe/s_e_cambs'
num_clips = len([name for name in os.listdir(seclipsdir) if os.path.isfile(os.path.join(seclipsdir, name))])
if (num_clips > 0):
  tracks.append('/home/liquidsoap/radio/elex/idents/s_e_cambs_trail.mp3')

# Add a random track
rndTrack = random.choice(list_of_playlist)
tracks.append(rndTrack)

# Add the SE Cambs package (will be blank if none)
tracks.append('/home/liquidsoap/radio/elex/s_e_cambs_MP3WRAP.mp3')

# Call MP3 wrap to add it all together
for track in tracks:
  command = command + "\"" + track + "\" "
print command
os.system(command)
