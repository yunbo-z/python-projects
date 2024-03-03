import random
#The chr() function returns the character that represents the specified unicode.

# Welcome to the PyPassword Generator
# How many letters would you like in your passsword?
# How many symbols would you like?
# How many numbers would you like?
# Here is your password:

print('Welcome to the PyPassword Generator')
print('How many letters would you like in your passsword?')
letter_num = int(input())
print('How many symbols would you like?')
symbol_num = int(input())
print('How many numbers would you like?')
number_num = int(input())

letter_unicode = list((range(97,123)))
letter_capitalization = list ((range(65,91)))
letter_unicode.extend(letter_capitalization)
random_letter_unicode = random.sample(letter_unicode, letter_num)

symbol_unicode = list((range(33,48)))
random_symbol_unicode = random.sample(symbol_unicode,symbol_num)

num_unicode = list((range(48,58)))
random_num_unicode = random.sample(num_unicode,number_num)

random_pwd_unicode = []
random_pwd = []
pwd = ''
random_pwd_unicode.extend(random_letter_unicode)
random_pwd_unicode.extend(random_symbol_unicode)
random_pwd_unicode.extend(random_num_unicode)

for unicode in random_pwd_unicode:
    random_pwd += chr(unicode)
random.shuffle(random_pwd)

for item in random_pwd:
    pwd += str(item)  

print(f"Here is your password: {pwd}")


# character unicode
# print(chr(97))
# print(chr(122))

# print(chr(65))
# print(chr(90))

# print(chr(48))
# print(chr(57))

# print(chr(33))
# print(chr(47))

