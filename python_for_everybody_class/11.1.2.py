# I first wrote the code so I could understand it like this:
# import re
# fhandle = open("regex_sum_53588.txt")
# numbers = list()
# for line in fhandle:
#     matches = re.findall('\d+', line)
#     if not matches: continue
#     for match in matches:
#         numbers.append(int(match))
#
# print(sum)

# Then I rewrote it using list comprehension so that I can read/understand it
# when I come across it, but I think this is more error prone and harder to maintain
# in the long run
import re
fhandle = open("regex_sum_53588.txt")
print(sum([int(number) for number in re.findall('\d+', fhandle.read())]))




