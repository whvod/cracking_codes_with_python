import pyperclip

def main():
    my_message = 'Common sense is not so common.'
    my_key = 8


    cipher_text = encrypt_message(my_key, my_message)

    # print the encrypted string in ciphetext to the screen
    # IF there are spaces at the end of the string we add '|' aka a "pipe"
    print(cipher_text + '|')

    # copy the encrypte sting in a cipher_text tot the clipboard
    pyperclip.copy(cipher_text)


def encrypt_message(key, message):
    # each string in cipher text represents a column in the gird
    cipher_text = [''] * key

    # loop through each column in ciphertext
    for column in range(key):
        current_index = column

        # keep looping until current_index goes past the message length
        while current_index < len(message):
            # place the character at current_index in message
            # at the end of the current column in the cipher text list
            cipher_text[column] += message[current_index]

            # move current index over
            current_index += key

    # convert the cipher_text list into a single string value and return it
    return ''.join(cipher_text)


# if the transpo encrypt is run(instead of imported as a module) call 
# the main() function

if __name__ == '__main__':
    main()
