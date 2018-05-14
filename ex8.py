# print the replacment fields in the order I want, otherwise it would replace
# {} in the order of 0, 1, 2, 3, 4 , ..., 

#V this way flops it backwards

#formatter ="{3} {2} {1} {0}"

#V this way is standard
formatter = "{} {} {} {}"

# print the 
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
	))
print(formatter.format(3,2,1,0))
print()
print()
print()
print()