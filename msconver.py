import json
from os import write


def convert_ticks(ticks):
    sec = int((ticks / 1000) % 60)
    min = int((ticks / 1000) / 60)
    frames = int((ticks % 1000) * 0.076)
    #print('{0:02d}'.format(min) + ":" + '{0:02d}'.format(sec) + ":" + '{0:02d}'.format(frames))
    return str('{0:02d}'.format(min) + ":" + '{0:02d}'.format(sec) + ":" + '{0:02d}'.format(frames))
    

def write_line(f, line):
    f.write(line + "\n")


fp = 'lp_die-zauberflte_wolfgang-amadeus-mozart-nicolai-gedda-gund_segments.json'
f = open (fp, "r") 
# read from from file
data = json.loads(f.read())

tracknum = 0
for disk in data:
    fn = disk['file']
    f = open( fn + ".cue", "w")
    fn = fn[fn.find('/') + 1:]

    #FILE "test.mp3" MP3
    write_line(f, "FILE " + fn + " FLAC")

    duration = 0
    timestamp = "00:00:00"
    for track in disk['tracks']:
        tracknum += 1

        #  TRACK 01 AUDIO
        write_line(f, "  TRACK " + '{0:02d}'.format(tracknum) + " AUDIO")

        details = track['file_tags']
        #TITLE "Nr. 1 Introduktion"
        write_line(f, "    TITLE \"" + details['TITLE'] + "\"")

        #PERFORMER "Wolfgang Amadeus Mozart; Nicolai Gedda; Gundula Janowitz; Walter Berry;
        write_line(f, "    PERFORMER \"" + details['ARTIST'] + "\"")

        #PREGAP 00:00:00
        start = int(track['segments']['final']['start'])
        #write_line(f, "    PREGAP " + convert_ticks(start))
        #INDEX 00 34:21:37
        #write_line(f, "    INDEX 00 " + timestamp)
        #timestamp = convert_ticks(track['segments']['initial']['end'])

        #INDEX 01 00:00:00
        write_line(f, "    INDEX 01 " + convert_ticks(start))
        #timestamp = convert_ticks(duration)       

    f.close()
    tracknum = 1
        





