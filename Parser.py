import matplotlib.pyplot as plt

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
            log_file.write(line)
            
    plot(PARSED_FILE)
def plot(FILENAME):
    y = []
    x = []

    timestamp = ""
    with open(FILENAME) as file:
        counter = 1
        for line in file:
            line = clean(line)

            if line != "":                      #sorts based on the second

                list = str.split(line)
                if len(list[1]) != 15:
                    continue

                if list[1][:-10] == timestamp:
                    counter += 1
                else:
                    print counter
                    timestamp = list[1][:-10]
                    print timestamp
                    second = timestamp.replace(":", "")

                    x.append(int(second))

                    y.append(counter)
                    counter = 1

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x,y, 'ro-')
    for xy in zip(x,y):                                       # <--
        ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--

    plt.grid()
    plt.show()

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