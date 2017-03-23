name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 #Inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inch = 25
inch_to_centimetre = 2.54 * inch

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy" % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee" % teeth
print "%d inches is equal to %d centimetres" % (inch,inch_to_centimetre)

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)