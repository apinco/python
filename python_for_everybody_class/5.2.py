highest = None
lowest = None
inum = None

while True:
    snum = input("Enter number: ")
    if (snum == "done" or snum == "Done"):
        break
    try:
        inum = int(snum)
    except:
        print("Invalid input")
        continue
    if highest is None:
        highest = inum
    if lowest is None:
        lowest = inum
    if inum < lowest:
        lowest = inum
    if inum > highest:
        highest = inum

print("Maximum is", highest)
print("Minimum is", lowest)


