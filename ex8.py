#Skeleton for formatter strings
formatter = "%r %r %r %r"
# All values placed after % in brackets, seperated by commas
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
# Placing formatter as a string returns the formatter value, rather than probing for new sets
print formatter % (formatter,formatter,formatter,formatter)

print formatter % (
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing.",
	"So I said goodnight."
	)