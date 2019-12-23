# x_arg convetion
# tuple data structures is used...
# arguments are passed as tuple



def printNames ( *names ) :
    for i in names :
        print ( i )


printNames ("Vipin","Nirala","Karan")




def addition ( *number ) :
    sum = 0

    for i in number :
        sum += i

    print ( sum )




addition ( 1,2,2,3,3,4,4,4,4,44,4,600 )