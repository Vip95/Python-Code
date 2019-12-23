marks = [ 99,90,100,55,67 ]

# Slice the list

# Print the entire lits
print ( marks[:] )

# Give starting index
print ( marks [ 2:] )

# GIve end index
print ( marks [ : 3 ] )

# Giving both
print ( marks [ 2:5 ] )


# Skipping 
# List will keep on skipping by 2
print ( marks [ 0: 5: 2] )



# Applying functions to the list
print (marks.reverse ())
# Will return None


print ( marks )


# Sort
marks.sort ()
print ( marks )



# Append
marks.append ( 10 )
print ( marks )

# insert 
marks.insert ( 3,300 )
print ( marks )

# pop
marks.pop ()
print (marks)