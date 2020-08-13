import random
import string
# список слов для игры
word_list = ('python', 'java', 'kotlin', 'javascript')


def word_conversion(string):
    secret_string = len(string) * '-'
    return secret_string


def one_char_check(char):
    if len(char) != 1:
        print('You should input a single letter')
        print()
        return True


def ascii_lowercase_check(char):
    if char not in string.ascii_lowercase:
        print('It is not an ASCII lowercase letter')
        print()
        return True


def input_list_check(char, list):
    if char in list:
        print('You already typed this letter')
        print()
        return True


def hangman():
    word = random.choice(word_list)
    hidden = word_conversion(word)
    hidden = list(hidden)
    word = list(word)
    out = ''
    life = 8
    input_list = []
    print()
    # цикл игры, выполняется пока жизней не станет ноль
    while life > 0:
        # вывод случаейного скрытого слова, которое загаданно
        print(out.join(hidden))
        # приглашение на ввод
        print('Input a letter: > ')
        char = input()
        # проверка ввода
        if one_char_check(char):
            continue
        if ascii_lowercase_check(char):
            continue
        if input_list_check(char, input_list):
            continue
        else:
            input_list.append(char)
        # основной код игры
        if char not in word:
            print('No such letter in the word')
            life -= 1
        for i in range(len(word)):
            if word[i] == char:
                hidden[i] = word[i]
        if life < 1:
            print('You are hanged!')
            break
        if word == hidden:
            print(f'You guessed the word {out.join(hidden)}!')
            print('You survived!')
            print()
            break
        print()


# приветствие
print("H A N G M A N")
# меню игры
while True:
    print('Type "play" to play the game, "exit" to quit:')
    menu = input()
    if menu == 'play':
        hangman()
    elif menu == 'exit':
        break
