import sys, os

constituency=sys.argv[1]

clipsdir =  "/home/liquidsoap/radio/elex/clips/" + constituency
clipsout =  "/home/liquidsoap/radio/elex/clips_safe/" + constituency

for filename in os.listdir(clipsdir):
    if filename.endswith(".wav"): 
        if os.path.isfile(os.path.join(clipsout, filename.replace(".wav",".mp3"))):
           # Do nothing
           continue
        else:
           command = "ffmpeg -i \"" + os.path.join(clipsdir, filename) + "\" -ab 192k -ac 2 -ar 44100 \"" + os.path.join(clipsout, filename.replace('.wav','.mp3')) + "\""
    	   os.system(command)
           continue

    if filename.endswith(".mp3"): 
        if os.path.isfile(os.path.join(clipsout, filename)):
           # Do nothing
           continue
        else:
           command = "ffmpeg -i \"" + os.path.join(clipsdir, filename) + "\" -ab 192k -ac 2 -ar 44100 \"" + os.path.join(clipsout, filename) + "\""
    	   os.system(command)
           continue
