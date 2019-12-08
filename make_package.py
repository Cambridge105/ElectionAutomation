import sys, os, os.path, random, glob, datetime

constituency=sys.argv[1]

# Check whether files exist in clips dir for the constituency
clipsdir = '/home/liquidsoap/radio/elex/clips_safe/' + constituency
num_clips = len([name for name in os.listdir(clipsdir) if os.path.isfile(os.path.join(clipsdir, name))])
timenow = datetime.datetime.now()

#f = open("/home/liquidsoap/radio/elex/" + constituency + ".m3u", "w")
command = "mp3wrap /home/liquidsoap/radio/elex/" + constituency + ".mp3 "

os.system ("rm /home/liquidsoap/radio/elex/" + constituency + "_MP3WRAP.mp3")
 
if (num_clips <1):
  f = open("/home/liquidsoap/radio/elex/" + constituency + "_MP3WRAP.mp3", "w")
  f.write("")
  f.close()
  exit()
 

command = command + ("/home/liquidsoap/radio/elex/idents/ident_" + constituency + ".mp3 ")
list_of_files = glob.glob(clipsdir + '/*.mp3')
tryresults = os.path.join(clipsdir, "results.mp3")
if (os.path.isfile(tryresults)):
  command = command + tryresults + " "
  list_of_files.remove(tryresults)
if (len(list_of_files) > 0):
  latest_file = max(list_of_files, key=os.path.getctime)
  command = command + "'" + latest_file + "' "
  list_of_files.remove(latest_file)
if (len(list_of_files) > 0):
  latest_file = max(list_of_files, key=os.path.getctime)
  command = command + "'" + latest_file + "' "
jingle = random.choice(os.listdir("/home/liquidsoap/radio/elex/jingles/"))
print (command)
command = command + "'/home/liquidsoap/radio/elex/jingles/" + jingle + "'"
os.system(command)

