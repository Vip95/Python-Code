# r+ can perform both read and write

file = open ( "file.txt", "r+" )

# Read the file
print ( file.read ( ) )
file .write ("Ram Ram Ji")
print ( file.read ( ) )
