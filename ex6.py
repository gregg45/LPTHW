# x is assigned the value of string with a format character that can replace numbers
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# y is assigned using the two previously assigned variables of binary and do_not
y = "Those who know %s and those who %s." % (binary,do_not)
# variables x and y are printed
print x
print y
# The strings are printed within another string showing you can add strings on to other strings
print "I said %r." % x
print "I also said '%s'" % y

hilarious = False
# joke_evaluation calls on a variable but does not immediately assign with brackets
joke_evaluation = "Isn't that joke so funny?! %r"
# the variable is then called on this line and it takes up the value assigned separated by percentage
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

# string concatenation 

print w + e