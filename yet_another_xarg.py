# Let's mix up the x_arg with a normal argument
# Remember : You need to use x_arg as last argument in the function


def function ( name, *numbers ) :
    print ( name ) 

    for i in numbers :
        print ( i )




function ("Vipin",1,2,2,3,3,3,3,3,4,4,4,4,420)