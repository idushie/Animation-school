def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    if '.' in text or ',' in text:
        new_txt = ''
        for index, letter in enumerate(text):
            if letter == '.' or letter == ',':
                new_txt = text[:index] + text[index:]
        print (new_txt)
        
    res = text.split(' ')

    res = [value for value in res if value]

    return res[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")