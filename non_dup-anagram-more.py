
# merge sort counting inversions

# Anagram detection

def is_anagram(str1, str2):
  # Create a dictionary to store the frequency of each character in the first string.
  char_counts = {}
  for char in str1:
    if char not in char_counts:
        char_counts[char] = 1
    else:
        char_counts[char] += 1
    

  # Iterate over the characters of the second string and decrement the corresponding count in the dictionary.
  for char in str2:
    if char not in char_counts:
      return False
    char_counts[char] -= 1

  # If all counts in the dictionary are zero, the strings are anagrams.
  return all(count == 0 for count in char_counts.values())


# Example usage:
# print(is_anagram("hello", "olleh"))  # True
# print(is_anagram("hello", "world"))  # False




# print(anagram_detection(word1, word2))



# Given a text file, find the 10 most common words in the dictionary.

# Find a non-duplicate character in a string of user input

word3 = 'AAddrriaann'

def non_duplicate(word9):
    word_dict = {}
    result = []
    for char in word9:
        if char not in word_dict:
            word_dict[char] = 1
        else:
            word_dict[char] += 1
    for key, value in word_dict.items():
        if value == 1:
            result.append(key)
    return result
  
print(non_duplicate('Addriiaann'))
#print(f'The first non-duplicate character is: {result}')


# You have a linked list. Return the second to last element

# List reversal, in place.

#string reversal question without using string functions 

word5 = 'Adrian'
def string_reverse(word5): # or use python [::-1] or for i in reversed(word5):
    new_str = ''
    for i in range(len(word5)-1, -1, -1):
        new_str = new_str + word5[i]

    return new_str

# print(string_reverse(word5))



def get_most_common_words(file_path, num_words=10):
    # Read the text file and extract words
    with open('log.txt', 'r') as file:
        text = file.read()
    # Convert the text to lowercase and split it into words
    words = text.lower().split()
    # Create a dictionary to store word frequencies
    word_counts = {}
    # Count the occurrences of each word
    for word in words:
        # Remove punctuation (replace with an empty string)
        word = word.strip(".,!?();:'\"")
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    # Sort the words by frequency without using key=lambda
    sorted_words = sorted(word_counts.items(), reverse=True)
    # Get the most common words
    most_common_words = sorted_words[:num_words]
    return most_common_words

# Replace 'your_file.txt' with the path to your text file
file_path = 'log.txt'

# Example usage:
most_common_words = get_most_common_words(file_path)

# Display the results
# print(f"The 10 most common words in the file '{file_path}' are:")
# for word, count in most_common_words:
#     print(f"{word}: {count} times")
