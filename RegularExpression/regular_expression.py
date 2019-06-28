import re

hand = open("Mailbox.txt")

for line in hand:
    line = line.rstrip()
    if re.search('^X\S*:',line):
        print(line)
