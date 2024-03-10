import random
from hangman_art import logo
# pick a random word
# show the underscore of each alphabet
# 6 ballons
Christmas_WinterHolidays = ['Christmas tree', 'Wreath', 'Stocking', 'Eggnog', 'Gingerbread', 'Yule log', 'Hanukkah', 'Kwanzaa', 'New Year’s Eve', 'Winter solstice']

print(logo)
print('Welcome to this hangman game!')
word = random.choice(Christmas_WinterHolidays).upper()
alphabet_space_list = []
alphabet_list = []
for alphabet in word:
    alphabet_space_list += '_'
    alphabet_list += alphabet


total_alphabet=0
wrong_answer = 0
while total_alphabet < len(word):
    count_underscore = alphabet_space_list.count('_')

    guess_alphabet = input('Guess an alphabet: ').upper()
    for i in range(len(word)):
        if guess_alphabet == word[i]:
            alphabet_space_list[i] = guess_alphabet
            total_alphabet += 1
    if count_underscore == alphabet_space_list.count('_'):
        print('Wrong Alphabet!')
        wrong_answer +=1
        if wrong_answer == 6:
            print('DEAD!')
            print(f"The correct word is '{word}'")
            break
    print(f"{' '.join(alphabet_space_list)}")