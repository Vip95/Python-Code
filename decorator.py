# First_method to create a decorator
def decorator ( function ) :
    def newFunction ( ) :
        print ("Executing now")
        function ()
        print ("Execution finished")
    return newFunction




def printHelloWorld ( ) :
    print ("Hello World")


result = decorator ( printHelloWorld )
result ()







# ----------Another method to create a decorator-----------------------




