file=open("hello.py")
for l in file.readlines():
    print(l.rstrip("\n"))