# Functions on dictionary


# How to make a copy
# You could just assing a dictionat to another var
# But here we might face a problem
# If we delete some object from one dictionary then that particular object also gets deleted from other one also
d1 = { "Name":"Vipin", "age" : 21 }
d2 = d1

print ( d2 )

del d2["age"]

print ( d2 )
print ( d1 )

# See... Both of the dictionaries are nothing but the refernce to the same dictionary




# SOLUTION
# USe dictionary.copy()

d3 = { "Name":"Vipin", "age": 21 }
d4 = d3.copy ()

del d4["age"]

print ( d4 )
print ( d3 )





#update a dictionary
d3.update ({"Course":"MCA" } )
print ( d3 )


# Print all the item and keys
for i in d3.keys() :
    print ( i )


# Print all the Items
for i in d3.items () :
    print ( i )