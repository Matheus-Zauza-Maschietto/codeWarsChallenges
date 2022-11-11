"""
A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is
 in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.
"""

def title_case(title, minor_words=''):
    return ' '.join([word.capitalize() if index == 0 or word.lower() not in [minor.lower() for minor in minor_words.split()] else word.lower() for index, word in enumerate(title.split())])
