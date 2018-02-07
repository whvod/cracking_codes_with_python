import random,sys, transpo_encrypt, transpo_decrypt

def main():
    random.seed(42) 

    for i in range(20):
        # generate random messages to test

        # the message will have a random length
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # convert the message string to a list to shuffle it
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # convert the list back to a stirng

        print('Test #%s: ''%s...''' % (i + 1, message[:50]))

        # check all possible keys for each message
        for key in range(1, int(len(message) / 2)):
            encrypted = transpo_encrypt.encrypt_message(key, message)
            decrypted = transpo_decrypt.decrypt_message(key, encrypted)

        # if the decryption doesn't match the original message, display
        # an erro message  and quit
        if message != decrypted:
            print('Mismatch with key %s and message %s.' % (key, message))
            print('Decrypted as: ' + decrypted)
            sys.exit()

    print('Transposition cipher test passed.')


# if transpo test is run (instead of imported as a module)
# call the main() function
if __name__ == '__main__':
    main()
