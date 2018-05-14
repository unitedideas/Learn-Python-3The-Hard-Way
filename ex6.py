
#creating a variable that contains the value of 10
types_of_people = 10
#creating a variable that contains V an f-string
x = f"There are {types_of_people} types of people."

#creating a variable that contains a string
binary = "binary"
#creating a variable that contains a string
do_not = "don't"
#creating a variable that contains an f-string
y = f"Those who know {binary} and those who {do_not}."

#printing the value of x
print(x)
#printing the value of y
print(y)

#printing an f-string
print(f"I said: {x}")
#printing an f-string
print(f"I also said: '{y}'")

#creating a variable that stores the value of False
hilarious = False
#creating a variable that contains an f-string
joke_evaluation = "Isn't that joke so funny?! {}"

#printing the formatting syntax to print the value stored in joke_evaluation and hilarious
print(joke_evaluation.format(hilarious))

#creating a variable that contains a string
w = "This is that left side of..."
#creating a variable that contains a string
e = "a string with the right side."

#printing the concatination the variables w and e
print(w + e)

#list of the variables in this script so I can check the type()
varlist = [types_of_people,x,binary,do_not,y,hilarious,joke_evaluation,w,e]

#looping through the list of vars to see what type each of them are.
for x, var in enumerate(varlist):
	print(type(varlist[x]))



