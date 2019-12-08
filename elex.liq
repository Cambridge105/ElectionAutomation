#!/usr/bin/liquidsoap
# Log dir
set("log.file.path","/tmp/basic-radio.log")


# Music
myplaylist = playlist("~/radio/elex/music.m3u")
# Some jingles
jingles = playlist("~/radio/elex/jingles.m3u")

headlinein = single("~/radio/elex/idents/headline_intro.mp3")
sequence = single("~/radio/elex/sequence_MP3WRAP.mp3")
irnsilence = single("~/radio/elex/idents/1sec_silence.mp3")
tothsilence = single("~/radio/elex/idents/1sec_silence.mp3")

# If something goes wrong, we'll play this
security = single("~/radio/elex/error.mp3")

# Start building the feed with music
radio = myplaylist

# Now add some jingles
radio = random(weights = [1, 3],[jingles, radio])

# And finally the security
radio = fallback(track_sensitive = false, [switch([({1m58s},sequence)]), switch([({29m57s},sequence)]), switch([({29m44s},headlinein)]), switch([({0m00s-1m59s},irnsilence)]), switch([({58m26s-59m59s},tothsilence)]), radio, security])


# Stream it out
output.icecast(%opus,
  host = "HOSTNAME", port = 8000,
  password = "PASSWORD", mount = "live",
  radio)

