import os
import string

file_num = 2

file = os.path.join('..', 'PyParagraph', 'paragraph_' + str(file_num) + '.txt')

paragraph_str = ''
with open(file, 'r', encoding = 'utf-8') as txtfile:
    paragraph_str = txtfile.read()
    
sent_count = paragraph_str.count('.') + paragraph_str.count('!') + paragraph_str.count('?')

letters = string.ascii_letters + " "

for i in paragraph_str:
    if i not in letters:
        paragraph_str = paragraph_str.replace(i, '')
        
paragraph_list = paragraph_str.split(" ")

letter_count = 0
for j in paragraph_list:
    letter_count += len(j)
    
word_count = len(paragraph_list)
avg_word_length = round(letter_count / word_count, 2)
words_per_sent = round(word_count / sent_count, 2)

output_file = os.path.join('..', 'PyParagraph', 'paragraph_analysis_' + str(file_num)+ '.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Paragraph Analysis\n--------------\nApproximate Word Count: ' + str(word_count) + '\nApproximate Sentence Count: ' + str(sent_count) + '\nAverage Letter Count: ' + str(avg_word_length) + '\nAverage Sentence Length: ' + str(words_per_sent))