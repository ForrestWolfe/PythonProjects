# Caesar cipher enter in a message. It will not decrypt where your spaces are in your message
text = input("Enter a passphrase: ")
# message to be stored.
cipher = ''
# calling the decrypted cipher the cracked variable.
cracked = ''
# iterating through the text string
for char in text:
    # if character isn't already capitalized then continue
    if not char.isalpha():
        continue
        # make the character/letter uppercase
    char = char.upper()
    # changing the order of the string by moving it to the next alphabetical character
    # ord(char) returns a number and by adding a number to that it changes that character to the next alphabetical character in the alphabet.
    code = ord(char) + 1
    # if the new letter is greater than  z the change it to a
    if code > ord('Z'):
        code = ord('A')
        # add the letter to the cipher string
    cipher += chr(code)

print('Your message "encrypted" with Caesars cipher: ' + cipher)

# decrypting the cipher with a for loop
for i in cipher:
    # if the character in the cipher is uppercase change it to lowercase
    if i.upper():
        i = i.lower()
        # change the order of the character by -1 from the order number of that alphabetical character
    code = ord(i) - 1
    # if the character is equal to ` change it to z
    if code == ord('`'):
        code = ord('z')
    # add the cracked character to the cracked string
    cracked += chr(code)

# print the results
print("Caesars cipher: \n\t\t" + cipher + "\b\n Caesars cipher decoded: \n\t\t" + cracked)