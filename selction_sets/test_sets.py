import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    letters_list = re.findall('[help]|[asap]', subj.lower())
    if letters_list and len(set(letters_list)) >= 4:
        return True

    letters_list = re.findall('[help]|[asap]', subj.lower())
    else:
        return False

if __name__ == '__main__':
    

    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful('H!E!L!P!') == True, 'Third'
    assert is_stressful('HHHEEEEEEEEELLP') == True, 'Forth'
    assert is_stressful('H-E-L-P') == True, 'Fith'
    assert is_stressful('something is gona happen') == False, 'Sixth'
    assert is_stressful('asap help') == True, 'Seventh'
    assert is_stressful('h!e!l!p') == True, 'Seventh'
    assert is_stressful('We need you A.S.A.P.!!') == True, 'Seventh'
    
    print('Done! Go Check it!')
