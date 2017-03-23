# import argv from sys module
from sys import argv
# unpacks argv to two variables
script, input_file = argv

# function print_all, which accepts variable f- for filename
def print_all(f):
	# print the read of the filename
	print f.read()

# this function will rewind to the beginning of the file
def rewind(f):
	# seek function moves the pointer to the beginnig of the f file
	f.seek(0)

# This function will print one line at a time
def print_a_line(line_count,f):
	# this print the current line number along with the contents of the line
	print line_count, f.readline(),
	#every time you use readline it goes down one more line it has nothing to do with the code below

# current file is assigned to the input file
current_file = open(input_file)

print "First let's print the whole file:\n"

# print all function is called
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# rewind function is called
rewind(current_file)

print "Let's print three lines:"

# current_line is assigned for printing the line number, print_a_line is called 3 times,
# each time incrementing current line_by one
current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line,current_file)