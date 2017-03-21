FILENAME = "fullLog3.txt"
PARSED_FILE = "parsed3.txt"

log_file = open(PARSED_FILE, "w")

with open(FILENAME) as file:
    for line in file:
        print line
        log_file.write(line)