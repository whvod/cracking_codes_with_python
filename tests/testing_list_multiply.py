symbols = 'abcdefgijklmnopqrstuvwxyz'

plaintext = [''] * 8

print(f'this is plaintext {plaintext}')

columns = 0

for symbol in symbols:
    plaintext[columns] += symbol
    columns += 1

