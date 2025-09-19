from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
SCORE_CHART = { "A":1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "R":1, "S":1, "T":1, 
            "D":2,"G":2, 
            "B":3, "C":3, "M":3, "P":3,
            "F":4, "H":4, "V":4, "W":4, "Y":4,
            "K":5,
            "J":8,"X":8,
            "Q":10,"Z":10
            }

def draw_letters():
    #this is the array that will be returned
    list_ten_strings = []

    #copy of the dictionary instead of using .copy
    letter_pool = LETTER_POOL.copy()

    #new list called bag to add the random keys frequency

    bag = []
        
    for a_single_letter, count in LETTER_POOL.items():
        for _ in range(count):
            bag.append(a_single_letter)

    while len(list_ten_strings) < 10:
        random_letter = randint(0, len(bag) -1)
        letter = bag[random_letter]
        list_ten_strings.append(letter)
        bag.pop(random_letter)

    return list_ten_strings
    pass

def uses_available_letters(word, letter_bank):

    letters_copy = letter_bank.copy()

    for letter in word:
        letter = letter.upper()
        if letter not in letters_copy:
            return False
        letters_copy.remove(letter)
    return True
        
def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
