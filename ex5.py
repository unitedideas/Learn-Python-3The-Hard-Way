centemeters = 2.54 #per inch
kilograms = 0.453592 #per pound
name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 * centemeters #inches
weight = 180 * kilograms #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print(f"Let's talk about {name}.")
print(f"He's {round(height)} centemeters tall.")
print(f"He's {round(weight)} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {round(height)}, and {round(weight)} I get {round(total)}.")