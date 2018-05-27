# More Printing

# Use the format function to turn the formatter variable into other strings
formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))

# Note that capitalization is important with true and false
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"try you",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))