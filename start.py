import service

words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
word = service.get_word(words)
template = []
for i in range(len(word)):
    template.append('_')
error = 0


print("Мы загадали слово попробуйте отгадать букву из него {}".format(str(''.join(template))))

while error != 4 and not service.player_win(template, word):
    letter = input("Введите букву: ")
    if service.check_letter(letter, word):
        service.letter_open(letter, template, word)
        print("Правильно теперь слово выглядит так {}".format(str(''.join(template))))
    else:
        error = service.mistake(error)
        print("Неправильно у вас осталось {} попыток".format(4 - error))

if str(''.join(template)) == word:
    print("Вы выиграли! Это слово {}".format(word))
else:
    print("Вы проиграли это было слово {}".format(word))