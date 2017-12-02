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
count = 0
for line in fhandle:
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words[1])
    count = count + 1
print("There were",  27, "lines in the file with From as the first word")





