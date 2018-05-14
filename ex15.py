#from module sys inporting function argv
from sys import argv
#creating variables that we need when executing this script
script, filename = argv
#creates var txt set = to the function open() on the filename which is given in the command line

#filename = input("name that file: ")
txt = open(filename)
#simple print of the variable filename
print(f"Here's your file {filename}:")
#calls the function print on txt.read which is on function open filename
print(txt.read())
txt.close()

#prints function and gets input from user
print("Type the filename again:")
file_again = filename
#creates var file_again and sets it to open the user input file
txt_again = open(file_again)
#prints the text in the file
print(txt_again.read())
txt_again.close()

