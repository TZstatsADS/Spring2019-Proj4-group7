import re

def isClean(cur_token):
    
    # Words longer than 20 chars is garbage
    if len(cur_token) > 20:
        return False
    
    # Number of punctuation in string is greater 
    # than number of alpha numeric characters
    alphanum = re.findall("[A-Za-z0-9]", cur_token)
    punc = re.findall("[^A-Za-z0-9]", cur_token)
    if len(punc) > len(alphanum):
        return False
    
    # ignoring first and last, if there are two or more 
    # different punctuation
    uniquepunc = len(set(re.findall("[^A-Za-z0-9]", cur_token[1:-1] )))
    if uniquepunc > 1:
        return False

    # if 3 identical characters in a row
    tmp4 = re.findall("([a-z\\d])\\1\\1", cur_token)
    if tmp4:
        return False
    
    # if num upper case is greater than num lowercase
    # and word is not all uppercase
    upper = re.findall("[A-Z]", cur_token)
    lower = re.findall("[a-z]", cur_token)
    if (len(upper) > len(lower)) and (len(upper) != len(cur_token)):
        return False
    
    # if all characters are alphabetic
    # and num constants is greater than 8 times the vowels
    # or vice versa
    vowels = re.findall("[AEIOUaeiou]", cur_token)
    constants = re.findall("[^AEIOUaeiou]", cur_token)
    if cur_token.isalpha() and (len(vowels) > len(constants) * 8 or len(constants) > len(vowels) * 8):
        return False
    
    # four or more consecutive vowels or 5 or more consecutive constants
    tmpv = re.findall("[AEIOUaeiou]{4,}", cur_token)
    tmpc = re.findall("[^AEIOUaeiou]{5,}", cur_token)
    if tmpv or tmpc:
        return False
    
    # if first and last chars are both lower case an any character upper
    lower_ends = cur_token[0] + cur_token[-1]
    if lower_ends.islower() and not cur_token.islower():
        return False
    
    # if normal word
    return True