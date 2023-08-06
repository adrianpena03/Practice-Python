# Functions for finding Palindrome

def is_palindrome(word):
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

print(is_palindrome("rotor"))


def pal(word):
    og_word = word.lower()
    new_word = word.lower()[::-1]
    if og_word == new_word:
        return True
    return False

print(pal("Aka"))

