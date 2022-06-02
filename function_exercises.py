def is_two(n):
    '''number 2 and string 2'''
    return n in (2, '2')
print(is_two(2))

def is_vowel(n):
    return n.lower() in 'aeiou' and len(n) == 1

def is_consonant(n):
    return n not in ('a','e','i','o','u','A','E','I','O','U') and len(n) == 1
print(is_consonant('b'))

def cap_if_consonant(word):
    for char in word:
        if char[0] in ('a','e','i','o','u','A','E','I','O','U'):
            return word
        else:
            return word.capitalize()

def calculate_tip(x,y):
    bill_amount = x
    tip_percentage = y
    tip = x * y
    return (f'${tip}')

def apply_discount(x,y):
    original_price = x
    discount_percentage = y
    final_price = x - x * y
    return (f'${final_price}')

def handle_commas(n):
    no_commas = int(n.replace(',' , ''))
    return no_commas

def get_letter_grade(x):
    if x <=100 and x >= 90 :
        print(f'{x} is an A')
    elif x >= 80:
        print(f'{x} is a B')
    elif x >= 70:
        x(f'{x} is a C')
    elif x >= 60:
        print(f'{x} is a D')
    elif x <= 59 and x >=0:
        print(f'{x} is an F')
    else:
        print('Invalid number')

vowels = ('a','e','i','o','u','A','E','I','O','U')
def remove_vowels(word):
    for char in word:
        if char in vowels:
            word = word.replace(char,'')
    return word

def remove_special_char(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])

def normalize_name(string):
    special_char_removed = remove_special_char(string)
    return special_char_removed.lower().strip().replace(' ', '_')

def cumulative_sum(list):
    x = 0
    sum_list=[]
    for n in list:
        x += n
        sum_list.append(x)
    return sum_list