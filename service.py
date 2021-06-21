import random

def get_word(words):
    return random.choice(words)


def check_letter(letter, word):
    return letter in word

def letter_open(letter, template, word):
    for i in range(len(word)):
        if word[i] == letter:
            template[i] = letter


def player_win(template, word):
    return str(''.join(template)) == word


def mistake(error):
    return error + 1


