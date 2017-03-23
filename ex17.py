from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print "Press Enter to copy"
raw_input()
out_file = open(to_file,'w')
out_file.write(indata)

print "Alright,all done."

out_file.close()