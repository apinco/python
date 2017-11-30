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
for line in fhandle:
    print(line.rstrip().upper())
    #line_count = line_count +1

#print("Line count: ", line_count)




