import re

words = ["maya", "A_super_bus_driver_001", "potato", "B_sport_car_091", "laptop","I hate regexp","icecream", "tomato", "candy"]

def find_word(words:list):

    list_words = []
    for word in words:
        if word[0].isupper():
            
            if 'car' or 'bus' or 'truck' in word:

                if '_' in word[-4]:

                    if re.search(r'\d{3}', word):

                        list_words.append(word)

    return list_words

a = find_word(words)
print (a)