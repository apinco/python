def open_file():
    fhandle = None
    while True:
        fname = input("Enter file name (leave blank to quit): ")
        if fname == '':
            print("No filename entered, exiting")
            quit()

        try:
            fhandle = open(fname)
            return fhandle
        except:
            print("Failed to open file: ", fname)


fhandle = open_file()
line_count = 0
total = 0.0

for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    first_space = line.find(' ')
    snumber = line[first_space:]
    total = total + float(snumber.strip())
    line_count = line_count +1

print("Average spam confidence:", total / line_count)





