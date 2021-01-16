import textutils, phoneutils
import pronouncing

#Calls all the necessary subfunctions and prints out the results.
def rhyme_scheme(text):

    text_split = textutils.strip(text)
    text_phone = phoneutils.strip_emphasis(phoneutils.cut_phone(phoneutils.phone(text_split)))
    homophones = phoneutils.compare(text_split, text_phone)

    return homophones

#Gives multiple homophones of the input word.
def give_rhyme(word):

    homophonez = pronouncing.rhymes(word)

    homophones = {homophonez.index(word) : word for word in homophonez}
    
    return homophones