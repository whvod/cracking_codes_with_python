import math, pyperclip

def main():
    my_message = 'Cenoonommstmme oo snnio. s s c'
    my_key = 8


    plain_text = decrypt_message(my_key, my_message)


    # print with a | called pipe character after it in case
    # there are spaces at the end of the decrypted message:
    print(plain_text + '|')


    pyperclip.copy(plain_text)


def decrypt_message(key, message):
    # the transpo decrypt function will simulate the 'columns' and 'rows' of 
    # the grid that the plain_text is written on by using a list
    # of string. First, we need to calculate a few values

    # the number of 'columns' in our transpostion gird
    num_of_cols = int(math.ceil(len(message) / float(key)))
    # the number of 'rows' in our grid
    num_of_rows = key
    # the number of shaded boxes in the last col of the gird
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(message)
    
    # each string in plaintext represents a column in the grid:
    plain_text = [''] * num_of_cols

    # the column and row variables point to where in the grid the next
    # character in the encrypted message will go
    columns = 0
    rows = 0

    for symbol in message:
        plain_text[columns] += symbol
        columns += 1 

        # if there are no more columns OR we are at a shaded box, go back
        # to the first column and the next row
        if(columns == num_of_cols) or (columns == num_of_cols - 1 and rows >= num_of_rows - num_of_shaded_boxes):
            columns = 0
            rows += 1


    return ''.join(plain_text)

# if the transpo decrypt is run instead of imported as a module
# call the main() function
if __name__ == '__main__':
    main()
