import urllib.request
import json
from pyfirmata import Arduino, util, STRING_DATA
import time

port = '#portacomarduino'

board = Arduino(port)

nomecanale = input("inserisci il nome del canale:  ")
idcanale = input("inserisci l'id del canale:  ")

key= "#apikey"

def GetFollowerNumber():

    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+idcanale+"&key="+key).read().decode('utf-8')


    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

    string = subs + "iscritti!"

    return string

while True:
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(nomecanale))
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(GetFollowerNumber()))
    time.sleep(60)
