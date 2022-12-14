q1 = """ How are Python dictionaries different from Python lists?
a.Python lists are indexed using integers and dictionaries can use strings as indexes
b.Python dictionaries are a collection and lists are not a collection
c.Python lists can store strings and dictionaries can only store words
d.Python lists store multiple values and dictionaries store a single value
"""
q2 = """ What is a term commonly used to describe the Python dictionary feature in other programming languages?
a.Closures
b.Sequences
c.Associative arrays
d.Lambdas
"""
q3 = """ (T/F) When you add items to a dictionary they remain in the order in which you added them.
a.False
b.True
"""
q4 = """ What is a common use of Python dictionaries in a program?
a.Computing an average of a set of numbers
b.Sorting a list of names into alphabetical order
c.Building a histogram counting the occurrences of various strings in a file
d.Splitting a line of input into words using a space as a delimiter
"""
q5 = """ Which method in a dictionary object gives you a list of the values in the dictionary?
a.items()
b.keys()
c.values()
d.all()
e.each()
"""

questions = {q1:"a",q2:"c",q3:"a",q4:"c",q5:"c"}

name = input("enter your name:")
print("hello",name,"welcome to the quiz world")
score=0

for i in questions:
    print()
    print(i)
    ans = input("enter the answer (a/b/c/d):")
    if ans==questions[i]:
        print("True,you got 1 point")
        score = score+1
        print("current score is:",score)
    else:
        print("False,you lost 1 point")
        score = score -1
        print("current score is:",score)
print("Final score is:",score)