# Initialize vars
f_score = 0
letter_grade = ''

# Get score and validate it
s_score = input("Enter your score: ")
try:
    f_score = float(s_score)
except:
    print("Failed to type in a valid number\n")
    exit()

if (f_score < 0.0 or f_score > 1.0):
    print("blah")
    exit()

# Map number to letter grade
if (f_score >= 0.9):
    letter_grade = 'A'
elif (f_score >= 0.8):
    letter_grade = 'B'
elif (f_score >= 0.7):
    letter_grade = 'C'
elif (f_score >= 0.6):
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(letter_grade)