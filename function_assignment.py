# We can copy the code of the one function to other finction
# By the means of assignment operator

def function1 ( ) :
    print ( "Hi I have been called" )



# Create another function
function2 = function1



# Function2 will exist even though function is going to be deleted
del function1


# Call the function
function2 ()