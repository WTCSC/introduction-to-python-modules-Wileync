#define our count character function
def count_chars(text):
    #creates a variable "amtofchars" that equal the individual character length of the text
    amtofchars = len(text) 
#returns the amtofchars that were counted
    return(amtofchars)


#define our count words function
def count_words(text):
#creates a variable that is equal to the text after having been split between spaces
  textsplit = text.split()
#creates a variable "amtofwords" that is equal to the length of the text having been split at spaces
#this means that it will cound every word and stop and start at the spaces
  amtofwords = len(textsplit)
#returns the amtofwords that were counted in the text
  return(amtofwords)



#define our count sentences function
def count_sentences(text):
#sets up sn if statement that will return 0 if there is an empty text
  if count_chars(text) == 0:
#returns us 0
    return(0)
  # creates a variable that will count how many periods are in the text
  amtofperiods = text.count('.') 
# creates a variable that will count how many exclaimation points are in the text
  amtofexclaims = text.count('!')
# creates a variable that will count how many question marks are in the text
  amtofquests = text.count('?')
#creates a variable that will look at the last character in the text
  lastchar = text[-1]
# says that if the last character of the text isn't a '.' or a '!' or a '?' then it will add one to the sentences count
# this means that if the last character is a letter like someone forgot the final punction or its conversatonal
#then it will add one to count for the last sentence
  if lastchar not in ['.', '!', '?']:
#adds the 1 for the last sentence
    addone = 1
#says if the last character is a '.' or a '!' or a '?' then it wont add one, it will add 0 or nothing
  else:
#adding the 0
    addone = 0

#returns the total amount of periods, exclaimation points, and question marks, as well as the addone
#this gives us our total number of sentences.
  return(amtofperiods + amtofexclaims + amtofquests + addone)
