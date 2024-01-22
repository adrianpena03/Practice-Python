# Functions for finding Palindrome

# def is_palindrome(word):
#     start = 0
#     end = len(word) - 1
#     while start < end:
#         if word[start] != word[end]:
#             return False
#         start = start + 1
#         end = end - 1
#     return True

# print(is_palindrome("adrian"))


# def pal(word):
#     og_word = word.lower()
#     new_word = word.lower()[::-1]
#     if og_word == new_word:
#         return True
#     return False

# print(pal("Aka"))


# 1. Reverse each word in a sentence
# -------------------------------------

sentence = 'Hi, I am Adrian.'

def reverseSentence(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# print(reverseSentence(sentence))

# 2. Determine if the first and last numbers in a list are the same

lis = [1, 2, 3, 4, 5, 1]
def firstLast(lis):
    start = 0
    end = len(lis) - 1
    if lis[start] != lis[end]:
        return False
    return True

# print(firstLast(lis))

# Determine if a word is a palindrome
word1 = 'racecar'
word2 = 'racecar'
def isPalindrome(word1, word2):
    low_word1 = word1.lower()
    low_rev_word2 = word2.lower()[::-1]
    if low_word1 == low_rev_word2:
        return True
    return False

# print(isPalindrome(word1, word2))
    

    


