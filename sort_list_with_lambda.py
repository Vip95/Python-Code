# Sort the list using lamda fucntion

myData = [ [1,100], [2,90], [3,80] ]
# Sort the list by second element inside the list
myData.sort ( key = lambda myData : myData [1] )
print ( myData )