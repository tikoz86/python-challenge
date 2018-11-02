import os
import string

#choose file number
file_num = 1

#sets file
file = os.path.join('..', 'PyParagraph', 'paragraph_' + str(file_num) + '.txt')

#open and read file
paragraph_str = ''
with open(file, 'r', encoding = 'utf-8') as txtfile:
    paragraph_str = txtfile.read()

#sentence count    
sent_count = paragraph_str.count('.') + paragraph_str.count('!') + paragraph_str.count('?')

#creates a string
letters = string.ascii_letters + " "

#loop through paragraph and deletes all characters that are not letters 
for i in paragraph_str:
    if i not in letters:
        paragraph_str = paragraph_str.replace(i, '')

#splits the words         
paragraph_list = paragraph_str.split(" ")

#counts all letters
letter_count = 0
for j in paragraph_list:
    letter_count += len(j)

#counts all words    
word_count = len(paragraph_list)

#calculates average words
avg_word_length = round(letter_count / word_count, 2)

#calculates words per sentence
words_per_sent = round(word_count / sent_count, 2)

#sets output file
output_file = os.path.join('..', 'PyParagraph', 'paragraph_analysis_' + str(file_num)+ '.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Paragraph Analysis\n--------------\nApproximate Word Count: ' + str(word_count) + '\nApproximate Sentence Count: ' + str(sent_count) + '\nAverage Letter Count: ' + str(avg_word_length) + '\nAverage Sentence Length: ' + str(words_per_sent))