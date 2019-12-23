# Sort the list


def sortBySecondElement ( data ) :
    return ( data[1] )



myData = [ [1,55], [6,2], [9,1] ]
# Sort the list by second element of the list of list
myData.sort ( key = sortBySecondElement )
print ( myData )