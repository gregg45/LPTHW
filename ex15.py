#first we import argv to take arguement variables from the command line
from sys import argv
# next we unpack argv to the two variables specified
script, filename = argv
# we then assign the txt variable to a file which we open called filename, taken from the command line
txt = open(filename)

# We print a sentence with character formatting and with the filename
print "Here's your file %r" % filename
# we read the file text and print it
print txt.read()
# we ask for the file from the raw input
print "Type the filename again:"
file_again = raw_input("> ")
# we do the same thing, assigning it the variable text again
txt_again = open(file_again)

print txt_again.read()