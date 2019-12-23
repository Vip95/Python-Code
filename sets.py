# Set is a collection of well defined objects
numbers = [1,1,1,1,2,2,2,2,23,3,3,3,3,3,4]
mySet = set ( numbers )
print ( mySet )

# Only well defined objects are added into the set



# add
mySet.add ( 100 )
print ( mySet )



# union
set1 = {1,2,3,4}
set2 = {3,4,5,6,7}
print ( set1 | set2 )

# Intersection
print ( set1 & set2 )

# Difference 
print ( set1 - set2 )

# Sy diff
print ( set1 ^ set2 )