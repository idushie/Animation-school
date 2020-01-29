
def findMaxWord(*words:str):

    result = None

    list_length =[len(word) for word in words]

    max_word_length = max(list_length)

    word_index = list_length.index(max_word_length)

    result = words[word_index]

    return result

maxWord = findMaxWord('pineapple', 'polinomial', 'equaion')
print(maxWord)

