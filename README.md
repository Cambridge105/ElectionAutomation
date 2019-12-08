# ElectionAutomation
Automation of Cambridge 105 Radio's overnight election coverage

This repository contains the code files for running overnight election coverage. The idea is that correspondents at the counts have access to a Dropbox folder, where they file their reports. These are then automatically played out during overnight automation, accompanied by a few pre-recorded phrases.

## Pre-requisites
* ffmpeg
* MP3WRAP
* Liquidsoap
* Icecast server
Tested on Ubuntu 16.04 

## The clock hour:
* xx:00:00 - Silence (for IRN)
* xx:01:58 - Start playing a sequence file, called sequence_MP3WRAP.mp3
* When the sequence file ends, play jingles and music in a 1:3 ratio (where the music list is stored in music.m3u and the jingles in jingles.m3u)
* xx:29:44 - Play a headline intro
* xx:29:57 - Play a repeat of IRN from the top of the hour
* xx:31:57 - Play the sequence file again
* xx:58:27 - Silence (for TOTH sequence)
This is all based on a 3 second delay to TX.

## The sequence file:
The sequence file is made up of a number of other files, central to which are the three per-constituency package files: <constituency>_MP3WRAP.mp3

## The constituency package files are formed of an intro, the packages from the Dropbox (a file called results.mp3 / results.wav first, then the next two latest clips) and an outro and a jingle. If there are no clips, the whole file is 0 bytes (ie we don't intro when there's nothing to intro)

## Making files safe
Because we don't know exactly what format of MP3 / wav (bit rate, sample rate, channels) the correspondents will add to the dropbox, everything is re-sampled by ffmpeg and re-saved in a clips_safe/ directory 

## The cronjob
All of this is orchestrated by the cronjob, which: 
* rsyncs the clips from Dropbox to the clips/ directory
* grabs the IRN news after publication so it's ready to repeat
* runs ffmeg to resample IRN as it's provided mono
* runs convert_wav_mp3.py to resample clips and re-save them in clips_safe/ (note the filename is misleading, it actually does resample mp3s as well as wavs)
* runs make_package.py for each consitutency to create the three packages, which uses MP3WRAP to create the package file itself 
* runs make_sequency.py to create the sequence file (must be done after the packages are ready), again calling MP3WRAP

Be aware that MP3WRAP has no 'quiet' flag and prompts on file-overwrite, so we delete the existing file each time before starting.

## Running it
liquidsoap elex.liq


