import time 

initialTime = time.time ()


for i in range ( 45 ) :
    print ("Hello World")

# print the time
print ( time.time () - initialTime )



initialTime2 = time.time ()
k = 0
while ( k < 45 ) :
    print ( "Hello World" )
    k += 1

# print the time
print ( time.time () - initialTime2 )


 