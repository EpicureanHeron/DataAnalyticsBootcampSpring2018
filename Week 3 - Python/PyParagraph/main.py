import re

# open paragraph
f = open("paragraph_2.txt", "r")

# breaks into sentences
sentences = re.split(r"[.!?;]", f.read())

# initialize lists & variables
sentence = []
words = []
word_count = 0
character_count = 0

# split into words
for i in range(0, len(sentences) - 1):
    sentence.append(sentences[i])
    words.append(sentence[i].split())

# count number of sentences
sentence_count = len(sentences) - 1

# count total words in paragraph
for word in words:
    word_count += len(word)
    # get character count
    for character in word:
        character_count += len(character)

# calc average number of words in sentence
average_words = word_count / sentence_count

# calc average number of characters in words
average_character = character_count / word_count

# print results
print("Approximate Word Count: " + str(word_count))
print("Approximate Sentence Count: " + str(sentence_count))
print("Average Letter Count: " + str(round(average_character, 1)))
print("Average Sentence Length: " + str(round(average_words, 1)))