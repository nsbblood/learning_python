myString = 'My name is Ryan Mitchell. I live in Boston'
print(myString)
print(myString.split('.'))

#

def cleanWord(word):
  """
  This function cleans a word by removing punctuation and converting to lowercase.
  """
  cleaned_word = ""
  for char in word:
    if char.isalnum():  # Check if character is alphanumeric (letter or number)
      cleaned_word += char.lower()  # Add lowercase letter
  return cleaned_word

myString = "Hello, world! This is not an example. You are not good at it"

filtered_words = [cleanWord(word) for word in myString.split() if len(cleanWord(word)) < 3]

print(filtered_words)

#
