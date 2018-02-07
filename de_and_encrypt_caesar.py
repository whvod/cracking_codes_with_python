import pyperclip

message = 'This is my secret message.'

key = 13

mode = 'decrypt' # can be set to decrypt/encrypt

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''

for symbol in message:
    # note: only symbols in the symbols string can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbol_index = SYMBOLS.find(symbol)


        # perform encryption/decryption
        if mode == 'encrypt':
            translated_index = symbol_index + key
        elif mode == 'decrypt':
            translated_index = symbol_index - key
        else:
            print('mode must be encrypt or decrypt')

        # handle wraparound, if needed:
        if translated_index >= len(SYMBOLS):
            translated_index  -= len(SYMBOLS)
        elif translated_index < 0:
            translated_index += len(SYMBOLS)

        translated += SYMBOLS[translated_index]

    else:
        # append the symbol without encrypting/decrypting
        translated += symbol


# output the translated string
print(translated)
pyperclip.copy(translated)
