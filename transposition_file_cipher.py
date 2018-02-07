import time, os, sys, transpo_encrypt, transpo_decrypt

def main():
    input_filename = 'frankenstein.txt'
    
    output_filename = 'frankenstein.encrypted.txt'
    my_key = 10
    my_mode = 'encrypt'

    # if the input file does not exist, the program terminates early
    if not os.path.exists(input_filename):
        print('The file %s does not exist. Quitting...' % (input_filename))
        sys.exit()

    # if the output file already exists, give the user a chance to quit
    if os.path.exists(input_filename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit' % (output_filename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()


    # read in the message from the input file
    file_obj = open(input_filename)
    content = file_obj.read()
    file_obj.close()


    print('%sing...' % (my_mode.title()))

    # measure how long the encryption/decrytion takes
    start_time = time.time()
    if my_mode == 'encrypt':
        translated = transpo_encrypt.encrypt_message(my_key, content)
    elif my_mode == 'decrypt':
        translated = transpo_encrypt.encrypt_message(my_key, content)
    total_time = round(time.time() - start_time, 2)
    print('%sion time: %s seconds' % (my_mode.title(), total_time))

    # write out the translated message to the output file
    output_file_obj = open(output_filename, 'w')
    output_file_obj.write(translated)
    output_file_obj.close()

    print('Done %sing %s.' % (my_mode.title(), output_filename))


# if transposition cipher file is run instead of imported as a module
if __name__ == '__main__':
    main()

