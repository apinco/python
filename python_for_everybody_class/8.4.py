fhandle = open("romeo.txt")

unique_list = list()
for line in fhandle:
    words = line.split()
    for word in words:
        if word not in unique_list:
            unique_list.append(word)

unique_list.sort()
print(unique_list)