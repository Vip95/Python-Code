# Compute factorial of the number

def factorial ( number ) :
    if ( number == 0 ) :
        return 1;
    else :
        return number * factorial ( number - 1 )





# User Input
number = int ( input ( "Enter a number") )

print ( factorial ( number ) )