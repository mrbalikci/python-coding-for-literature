# Import Needy libraries

import os
import csv

# The file path
file_path = os.path.join('resources', 'paragraph_1.txt')

# Empty Lists 
words = []
sentences = []
letter_counts = []

# Open the text file 
with open(file_path) as file:

    # read the text 
    text = file.read()

    # split the text by ''
    word = text.split()
    
    # split the text by '.'
    sentence = text.split('.')

    # append words and sentences to the empty lists 
    words.append(word)
    sentences.append(sentence)

    # calculate each word sizes
    for w in word:
        letter_counts.append(len(w))



# Average Letter Count
avg_letter_count = sum(letter_counts) / len(word)

# Average Sentence Length
avg_sent_lenght = sum(letter_counts) / len(sentence)

# Print the outputs 

print(f"There are total of {len(word)} words in this text file")
print(f"There are total of {len(sentence)} sentences in this text file")
print(f'There are total of {sum(letter_counts)} letters in this text file')
print(f'The average of letter count for this text per word is {avg_letter_count}')
print(f'The average of letter count for this text per sentence is {avg_sent_lenght}')
