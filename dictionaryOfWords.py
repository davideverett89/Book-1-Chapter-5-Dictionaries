# Dictionary of Words Exercise
"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["Clary"] = "To make a loud or shrill noise"
word_definitions["Vanjas"] = "The Australian pied crow shrike Strepera graculina It is glossy bluish black with the under tail coverts and the tips and bases of the tail feathers white"
word_definitions["Strockle"] = "A shovel with a turned up edge for frit sand etc"
word_definitions["Embarrassing"] = "hard to deal with as greeted with an embarrassing silence"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
word1 = word_definitions["Clary"]
word2 = word_definitions["Vanjas"]

print(word1)
print(word2)

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (word, meaning) in word_definitions.items():
    print(f"The definition of {word} is: {meaning}.")
