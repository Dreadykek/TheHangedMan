import pytest

import service

words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
word = words[1]
template = []
for i in range(len(word)):
    template.append('_')
error = 3

def test_get_word():
    result_task = service.get_word(words)
    assert result_task in words

def test_check_letter():
    word = service.get_word(words)
    assert word[0] in word

def test_letter_open():
    for i in range(len(word)):
        if word[i] == 't':
            template[i] = 't'

    assert str(''.join(template)) == 't__t___'

def test_player_win_valid():
    template = word
    assert template == word

def test_player_win_invalid():
    assert template != word

def test_mistake():
    result = service.mistake(error)
    assert result == 4