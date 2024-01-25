# Open a file
fo = open("foo.txt", "r+")
fo.write( "Python is a great language.\nYeah its great!!\n")

fo.write( "Indeed its nice\n")

data = fo.read()

print(f"{data}")

# Close opened file
fo.close()

