"""
By Soleil Vivero
04/03/21
"""

from tkinter import *

root = Tk()
root.title('Word Count')

txtbox = Text(root, padx=10, pady=10, wrap=WORD)
wordCountLabel = Label(root, padx=10, pady=5, text='Word Count:')


def word_counter():
    num = 0
    txt = txtbox.get(1.0, END)
    txt = txt[:-1]  # Removes the last character of the string since
                    # tk.Text attaches an empty character at the end
                    # of what you type in.
    txtLength = len(txt)

    for char, index in zip(txt, range(0, txtLength + 1)):
        if char in '1234567890':
            print(f'{index}, a number was passed')
            pass
        elif char == ' ':
            # If there are double spaces, don't add a word
            if txt[index - 1] == ' ':
                print(f'{index}, double space')
                pass

            # Unless the character is "a" or "I", don't add a word if there is \
            # only one character between spaces
            elif txt[index - 1] != ' ' and txt[index - 2] == ' ':
                print(f'{index}, one char between spaces')
                if txt[index - 1] == 'a' or txt[index - 1] == 'I':
                    print('isolated character added')
                    num += 1
                else:
                    pass

            # Add a word if there is a space
            else:
                num += 1

            # If there is a space before the last character of the text or if \
            # the space is the last character, remove a word
            if (index + 1) == (txtLength - 1) or index == (txtLength - 1):
                print(f'{index}, either a space before the last character, ' \
                      'or a space is the last character')
                num -= 1

    wordCount = str(num + 1)
    wordCountLabel.config(text=f'Word Count: {wordCount}')


def clear():
    txtbox.delete(1.0, END)


clear = Button(root, padx=5, pady=5, text='Clear', command=clear)
count = Button(root, padx=5, pady=5, text='Count', highlightbackground='Red',
               command=word_counter)

txtbox.grid(row = 0, column=0, columnspan=2)
clear.grid(row = 1, column=0)
count.grid(row = 1, column=1)
wordCountLabel.grid(row = 2, column=0, columnspan=2)

root.mainloop()
