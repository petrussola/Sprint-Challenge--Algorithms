'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # if initial word is less than 2 words, return 0
    # because it won't be possible for the word
    # to be "th"
    if len(word) < 2:
        return 0
    # Recursive component
    # If we are assessing the last 2 chars of the word
    # and if word matches 'th', return 1
    # elif len(word) == 2 and word == "th":
    #     return 1
    # # if the last 2 chars are not 'th', return 0
    # elif len(word) == 2 and word != "th":
    #     return 0
    # if word length is bigger than 2, then check 
    # the first 2 chars. If they match 'th' it means
    # that we should call teh recursion with our 
    # counter at 1. That is why we call 1 + recursion
    elif word[0:2] == "th":
        return 1 + count_th(word[1:])
    # if the first 2 chars are not 'th', then 
    # we call the recursion without any counter
    else:
        return 0 + count_th(word[1:])
