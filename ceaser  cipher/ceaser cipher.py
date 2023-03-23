from art import logo
import os


def ceaser(text, shift, direction,alphabet):
    encrypted_text = ""
    new_shift = 0
    for t in text:
        for i in range (0, len(alphabet)):
            new_shift = shift
            if t == alphabet[i]:
                 #while shift is greater than zero it will keep on add the index position by 1 from the location of the text.               
                if direction == 'encode':
                    while new_shift > 0:
                        #if the index point out of list and shifting is still remaining index position resets to 0
                        if i < len(alphabet)-1:
                            i+=1
                        else:
                            i=0
                        new_shift-=1

                elif direction == 'decode':
                    #if the index point out of list and shifting is still remaining index position resets to length of the list i.e last index point of the list
                    while new_shift > 0:
                        if i > 0:
                            i-=1
                        else:
                            i=len(alphabet)-1
                        new_shift-=1
                
                encrypted_text+=alphabet[i]

        if not t.isalpha():
            encrypted_text+=t
            
    return encrypted_text


def main():
    print(logo)
    #Taking input from the user
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    #calling function ceaser
    print(f"The {direction}d code is {ceaser(text, shift, direction,alphabet)}")

main()

# status = True

while input("do you still want to continue?\n Yes or No\n").lower() == 'yes':
    os.system('cls')
    main()

