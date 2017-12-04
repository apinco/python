import re
fhandle = open("regex_sum_53588.txt")
numbers = list()
for line in fhandle:
    matches = re.findall('\d+', line)
    if not matches: continue
    for match in matches:
        numbers.append(int(match))

print(sum(numbers))