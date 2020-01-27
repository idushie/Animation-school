words = ["maya", "A_super_bus_driver_001", "potato", "B_sport_car_091", "laptop","I hate regexp","icecream", "tomato", "candy"]

def find_word(words):
    num = [0,1,2,3,4,5,6,7,8,9]
    list_words = []
    for word in words:
        if word[0].isupper():
            
            if 'car' or 'bus' or 'truck' in word:

                if '_' in word[-4]:

                    if int(word[-3]) in num:
                        if int(word[-2]) in num:
                            if int(word[-1]) in num :
                                list_words.append(word)
    return list_words

a = find_word(words)
print (a)