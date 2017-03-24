import matplotlib.pyplot as plt
import sys

FILENAME = "fullLog3.txt"
PARSED_FILE = "parsed3.txt"
CHAN = "#smashstudios"                          #change as needed

def main():
    log_file = open(PARSED_FILE, "w")
    timestamp = ""
    with open(FILENAME) as file:
        counter = 1
        for line in file:
            line = clean(line)
            #print line
            log_file.write(line)

    log_file.close()
    plot(PARSED_FILE)


def plot(name):                 #plots responses vs time in 1 minute intervals
    y = []
    x = []

    first = firstline(name)

    list = str.split(first)             #gets initial timestamp
    timestamp = list[1][:-10]

    with open(name) as file:
        counter = 1
        for line in file:
            print line
            if line != "":                      #sorts based on the second

                list = str.split(line)
                if len(list[1]) != 15:          #skip any line with improperly formated timestamp
                    continue

                if list[1][:-10] == timestamp:
                    counter += 1
                else:
                    second = timestamp.replace(":", "")     #once timestamp changes, add the message count and stamp
                    x.append(int(second))
                    timestamp = list[1][:-10]
                    y.append(counter)

                    counter = 1
        x.append(int(timestamp.replace(":","")))        #final data points
        y.append(counter)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x,y, 'ro-')            #plot
    for xy in zip(x,y):                                       # <--
        ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--

    plt.grid()
    plt.show()

def firstline(name):
    with open(name) as file:
        return file.readline()

def clean(line):                  #tests for chat message
    list = str.split(line)
    if(len(list[0]) != 10):
        return "";
    data = list[0] + " " + list[1]
    for i in range (5, len(list)):
        data += " "
        data += list[i]
    return data + "\n"

main()