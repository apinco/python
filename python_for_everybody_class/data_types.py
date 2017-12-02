# Dicttionary
# Create using curly brackets
mydict1 = { 'adam' : 1, 2 : 2}
print(type(mydict1))
print(mydict1)
# Create using dict(), the downside is that you can only uses keys that are
# valid python identifiers.  so the below doesn't work if you uncomment 2=2 but works fine above
mydict1 = dict(
    adam=1,
#    2=2
)
print(type(mydict1))
print(mydict1)
print("")


# Lists
# Initialize using square brackets
mylist1 = [1,2,3]
print(type(mylist1))
print(mylist1)
#Initial using list() - This is really for creating an empty list that will be popoulated
# inside a data structure so you need to initialize first...otherwise, just use square brackets
mylist1 = list()
print(type(mylist1))
print(mylist1)
print("")



#Tuples
#Initialize a tuple just like a list, except use parentheses
mytuple1 = ('a', 'b', 'c')
print(type(mytuple1))
print(mytuple1)
print("")


# Using dictionaries with tuples to sort to sort a dictionary by the keys
scores = { 'adam' : 100, 'zane' : 10, 'scott' : 90}
print(type(scores))
print(scores)
print(sorted(scores.items()))
print("")


# Using dictionaries with tuples to sort to sort a dictionary by the keys
# Note that you have to use .items() to get back tuples and when you append, you need to create
# a reversed tuple with () and flipping the key/value pairs
# Note the reverse=True to the function sorted
scores = { 'adam' : 100, 'zane' : 10, 'scott' : 90}
tmp = list()
for k, v in scores.items():
    tmp.append( (v, k) )
print(type(tmp))
print(tmp)
print(sorted(tmp, reverse=True))
print("")