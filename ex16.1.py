from sys import argv

script, filename = argv

readthis = open(filename)
print readthis.read()
readthis.close()