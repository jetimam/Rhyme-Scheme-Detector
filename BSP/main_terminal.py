import textutils, phoneutils
import pronouncing

#Calls all the necessary subfunctions and prints out the results.
def rhyme_scheme():
    text = input('Please enter your text: \n')

    text_split = textutils.strip(text)
    text_phone = phoneutils.strip_emphasis(phoneutils.cut_phone(phoneutils.phone(text_split)))
    homophones = phoneutils.compare(text_split, text_phone)

    for key,value in homophones.items():
        print(key, ': ', value)

#Spits out multiple homophones of the input word.
def give_rhyme():
    word = input(" > Please enter the word: \n")
    
    homophone_temp = pronouncing.rhymes(word)

    homophones = {homophone_temp.index(word) : word for word in homophone_temp}

    for key,value in homophones.items():
        result = str(key) + ': ' + value
        print(result)

user_question = input("What do you wish to do? Enter its corresponding number. \n > 1. Check the rhyme scheme of a text. \n > 2. Get rhymes for a single word.\n")

if user_question == "1":
    rhyme_scheme()
elif user_question == "2":
    give_rhyme()