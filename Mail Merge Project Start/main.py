#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()



with open("Input/Letters/starting_letter.txt") as letter:
    txt = letter.read()
    for name in names:
        name = name.strip()
        x = txt.replace("[name]", name)
        y = x.replace("Angela", "Sajeesh")
        with open(f"Output/ReadyToSend/{name}.txt", "w") as output_letter:
            output_letter.write(y)

