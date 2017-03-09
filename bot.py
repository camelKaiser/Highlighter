import socket
import time
import re

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "jackalapples"
PASS = "oauth:ab0krnwwqxyonvg6d0cn5g1vattcgt"
CHAN = "#ogaminglol"
log_file = open("log.txt", "w")


s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        print(response)
        log_file.write(response)
