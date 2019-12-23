# Key-value Pair Data Structure
nickNames = { "Vikas":"Vikki", "Sanjeev":"Sanju", "Pankaj":"Chintu", "Vipin":"Vip","Karan":"Kaale" }
print ( nickNames )

print ( nickNames["Vipin"] )





# Dictionary inside Dictionary
foodPref = { "Vikas":"Roti", "Pankaj":"Fish", "Karan":"Eggs","Vipin":{
    "breakfast":"Eggs", "luch":"Kari", "dinner":"Biryani"
}}

print ( foodPref )
print ( foodPref["Vipin"] )

# Printing a particular object from a dictionary which is inside another dictionary
print ( foodPref["Vipin"]["luch"] )


# append to the dictionary
foodPref["Sanju"] = "Tea"
print ( foodPref )



# delete a particular entry from dictionary
del foodPref["Sanju"]
print ( foodPref )