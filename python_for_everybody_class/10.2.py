def open_file():
    fhandle = None
    default_fname = 'mbox-short.txt'

    while True:
        prompt = "Enter file name (Defaults to:", default_fname
        fname = input(prompt)
        # If len of the string is < 1, then we didn't get a filename so default
        # to the default_filename
        if len(fname) < 1:
            fname = default_fname

        try:
            fhandle = open(fname)
            return fhandle
        except:
            print("Failed to open file: ", fname)

fhandle = open_file()
hours = dict()
for line in fhandle:
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5]
    hour = time[:2]
    hours[hour] = hours.get(hour, 0) + 1

for h,c in sorted(hours.items()):
    print(h,c)






