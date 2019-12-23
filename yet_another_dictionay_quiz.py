# Create a vocab dictionary

# Our dictionary
dictionary = {"arcane":"Mysterious", "adroit":"Skillfull","altourist":"Selflessness","abration":"Temporary suspended"}

# Search a vocab
vocab = input ("Please enter a vocab ")


# Print the meaning of the query
try :
    print ( dictionary[vocab] )
except KeyError :
    do_you_know_this_word = input ("DO you know this word?")
    if ( do_you_know_this_word.lower() == "yes" ) :
        meaning = input ("Ok well! Now enter the meaning of the word")
        dictionary[ vocab ] = meaning
    else :
        print ("Well Fuck you then!")
        exit ()
finally :
    print ("Meaning of the query is ", dictionary[vocab] )