# skip one item after printing first
items = [ "Bhindi", "Kela", "Chocolate", "Strawberry", "Apple", "Gajjak" ]

# index starts at 0
for index, item in enumerate ( items ) :
    if ( index % 2 == 0 ) :
        print ( item )