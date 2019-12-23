# Quiz Time!!!
# Create a dictionary

myDictionary = {"Apple":"It's a red colored fruit", "Ball":"It's just a round object to play with","Cat":"An animal","Dog": "An animal which may eat your cat"}

search_key_word = input ("Please enter a word")



# Printing the value
try :
    print ( myDictionary[search_key_word] )
except KeyError :
    meaning = input ("Please the meaning of the word")
    myDictionary[search_key_word] = meaning
finally :
    print ( myDictionary[ search_key_word ] )