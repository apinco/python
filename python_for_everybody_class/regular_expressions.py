# You must import regular expressions
import re

# Use resarch to look for a string and return True if it is found
fhandle = open("mbox-short.txt")
for line in fhandle:
    if re.search('From:', line):
        print(line)