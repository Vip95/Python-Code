def lowerPattern ( number ) :
    for i in range ( 0, number + 1 ) :
        for j in range ( number + 1, 0  ) :
            print ("*", end = "" )
        print ("")


def upperPattern ( number ) :
    for i in range ( 0, number ) :
        for j in range ( 0, i + 1 ) :
            print ("*", end = "" )
        print ("")



lowerPattern ( 5 )
upperPattern ( 5 )