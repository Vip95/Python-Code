# use a xx_arg function


def printInfo ( **edu ) :
    for name, educationBackground in edu.items() :
        print ( name, education )




# Create a dictionary
education = { "Vipin" : "Computer Science", "Karan" : "Chemistry", "Vikas" : "Civil Engineering", "PK" : "Commerce" }
printInfo ( **education )