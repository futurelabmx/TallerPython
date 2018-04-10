# FutureLab
# Primer taller de python

import random

# ASCII ART
images = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

# Palabras a seleccionar
words = [
    "python",
    "django",
    "anaconda",
    "tensor",
    "apple",
    "unix",
    "google"
]

print()
print("B I E N V E N I D O   A   A H O R C A D O")
word = words[random.randint(0, len(words) - 1)]
tries = 0
new_word = list()
print(images[tries])
spaces = ['-'] * len(word)
print(spaces)


while True:
    letter = input("Introduce una letra: ")

    if letter in ''.join(spaces):
        print("¡Ya has introducido esta letra!")

    for i, j in enumerate(word):
        if j == letter:
            spaces[i] = letter

    if letter not in word:
        tries = tries + 1


    print(images[tries])
    print(spaces)

    if tries == 7:
        print("¡Has sido ahorcado!")
        print("La palabra era '{}''".format(word))
        break


    if ''.join(spaces) == word:
        print("¡Has adivinado!")
        break

print()
