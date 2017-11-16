# Import needed modules
import json
# Functions
def find_def(word):
    if (word in data):
        return str(data[word])
    else:
        print("Word doesn't exist")
        exit()

# Read data into a dictionary (which is really just a hash)
data = json.load(open("data.json"))

# Perl like looping
#for key in data:
#    print("key: " + str(key) + " value: " + str(data[key]))

#Python style loop, must more efficient that the above method
#for key, value in data.items():
#    print("key:" + str(key) + "value:" + str(value))

word = input("Enter a word to look up: ")
print(find_def(word))


