#This will clean up the entered text in order to process it.
def strip(input_text): 
    output = input_text.replace(".", "")
    output = output.replace(",", "")
    output = output.replace("!", "")
    output = output.replace("?", "")

    output = output.split()
    
    return output