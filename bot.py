#Cyrus Boushehri 4/5/17
import socket
from api_client import translate

server  = "localhost"                                          #Global settings
port    = 6667
channel = ["#ar", "#de", "#en", "#es", "#fa", "#fi", "#fr", "hi", "#ja", "#ko", "#pt", "#ru", "#zh-CHS"]
botnick = "Tanobb"
irc     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

irc.connect((server, port))                                    #Connect to server
irc.send(bytes("USER {0} {0} {0} {0}\n".format(botnick), "UTF-8"))
irc.send(bytes("NICK {}\n".format(botnick), "UTF-8"))

def format(input):
    return name = ircmsg.split('!',1)[0][1:]
    return lang = ircmsg.split('#')[1].split(' :')[0]
    return msg  = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]

def broadcast(name, lang, msg):
    for chan in channel:                                   #Send translated message
        if chan != "#"+lang:
            tr  = translate(chan.strip("#"), lang, msg)
            tex = "<{}> [{}] {} {}".format(name, lang, msg, tr)
            irc.send(bytes("PRIVMSG {} :{}\n".format(chan, tex), "UTF-8"))

for i in channel:                                              #Join channels
    irc.send(bytes("JOIN {}\n".format(i), "UTF-8"))
    
while 1:
    ircmsg = irc.recv(2048).decode("UTF-8").strip("\n\r")      #Get input
    print(ircmsg)
    
    if ircmsg.find("PING :") != -1:                            #Respond to server pings
        irc.send(bytes("PONG :pingis\n", "UTF-8"))
        
    if ircmsg.find("PRIVMSG") != -1:                           #Listen for messages
        format(ircmsg)
        broadcast(name, lang, msg)
    
    if ircmsg.find("JOIN"):
        format(ircmsg)
        broadcast(name, "SYS", "Has Joined {}".format(lang))
    
    if ircmsg.find("QUIT"):
        format(ircmsg)
        broadcast(name, "SYS", "Has Quit {}".format(lang))