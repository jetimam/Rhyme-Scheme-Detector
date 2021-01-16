import pronouncing

#The list of vowels which are analyzed in order to detect the words that rhyme.
vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']

#This will try and translate each and every word to their phonetic representations.
def phone(input_list):
    output_list = list(range(len(input_list)))

    for i in range(len(input_list)):
        try:
            output_list[i] = pronouncing.phones_for_word(input_list[i])
        except:
            Exception(IndexError)

    return output_list

#This will eliminate the optional phonetic representations and instead just pick one.
def cut_phone(input_list):
    temp_list = list(range(len(input_list)))

    for i in temp_list:
        try:
            temp_list[i] = input_list[i][0]
        except:
                Exception(IndexError)

    return temp_list

#This will cut out the emphases in the translations.
def strip_emphasis(input_list):
    output_list = []

    for ele in input_list:
        try:
            temp = ele.replace("0", "")
            temp = temp.replace("1", "")
            temp = temp.replace("2", "")
        except:
            Exception(IndexError)
        
        try:
            output_list.append(temp)
        except:
            Exception(UnboundLocalError)

    return output_list

#Sorts the inputted text.
def compare(original_text, phone_list):
    rhymes = {v: [] for v in vowels}
    
    for i in range(len(phone_list)):

        last_vowel = vowel_util(phone_list[i])

        for v in vowels:

            if last_vowel == v:
                rhymes[v].append(original_text[i])

    return rhymes

#Gets the last vowel of the word entered.
def vowel_util(e):
    temp = e.split()
    vowel_check = []

    for i in range(len(temp)):
        for j in range(len(vowels)):
            if temp[i] == vowels[j]:

                vowel_check.insert(0, vowels[j])

    return vowel_check[0]