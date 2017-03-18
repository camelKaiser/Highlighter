import socket
import time
import re
from datetime import datetime

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "jackalapples"
PASS = "oauth:ab0krnwwqxyonvg6d0cn5g1vattcgt"
CHAN = "#smashstudios"                          #change as needed
log_file = open("fullLog2.txt", "w")


s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

while True:                                                 #data collection
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":               #pong as needed
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        response = str(datetime.now()) + " " + response;    #attach timestamp
        print(response.encode("utf-8"))                     #encode to handle invalid chars and write to file
        log_file.write(response.encode("utf-8"));
