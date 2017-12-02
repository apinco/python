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
senders = dict()
for line in fhandle:
    if not line.startswith("From "):
        continue
    words = line.split()
    senders[words[1]] = senders.get(words[1], 0) + 1

max_sender = None
max_count = 0
for sender,count in senders.items():
    if max_sender is None or count > max_count:
        max_sender = sender
        max_count = count
print(max_sender, max_count)







