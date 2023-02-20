def alphabet_position(text):
    alfabeto = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
                  "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
                  "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
                  "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,
                  "y": 25, "z": 26}
    return "".join([str(alfabeto[letter])+" " if letter in alfabeto.keys() else "" for letter in text.replace(" ", "").lower()]).strip()

"""
fbupFmeimHKoyrDJsgpzlUQydGdjRzUrpqgneJuhzhIduIjRcGFeCiWBGTDYtBZjCxZTfqhPLMztmssVIQfYMTCaCiagrwekofec

'6 2 21 16 13 5 9 13 15 25 18 19 7 16 26 12 25 4 4 10 26 18 16 17 7 14 5 21 8 26 8 4 21 10 3 5 9 20 10 24 6 17 8 26 20 13 19 19 6 1 9 1 7 18 23 5 11 15 6 5 3'
should equal
'6 2 21 16 6 13 5 9 13 8 11 15 25 18 4 10 19 7 16 26 12 21 17 25 4 7 4 10 18 26 21 18 16 17 7 14 5 10 21 8 26 8 9 4 21 9 10 18 3 7 6 5 3 9 23 2 7 20 4 25 20 2 26 10 3 24 26 20 6 17 8 16 12 13 26 20 13 19 19 22 9 17 6 25 13 20 3 1 3 9 1 7 18 23 5 11 15 6 5 3'
"""
print(alphabet_position("fbupFmeimHKoyrDJsgpzlUQydGdjRzUrpqgneJuhzhIduIjRcGFeCiWBGTDYtBZjCxZTfqhPLMztmssVIQfYMTCaCiagrwekofec"))
