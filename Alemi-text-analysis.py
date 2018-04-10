#Sina Alemi
#DATA 620 9041
#Assignment 12.1

#This program will take a text file as input and create a list
#of the counts of each unique word. The top 30 words are displayed by word count.

import sys

#load stopwords file
stopwords = open('stopwords.txt', 'r').read()

#prompts user for file name, displays error message if file not found.
fname = input('Enter file name: ')
try:
    f = open(fname, 'r').read().split() #parse text to individual words
except:
    print('Invalid file name:', fname, '\nexiting...')
    sys.exit()



#create list of all words in txt that are NOT stopwords, and join them into one string
lowerWords = [word.lower() for word in f] #convert to lower case
filteredFile = [word for word in lowerWords if word not in stopwords]   
filteredFile = ' '.join(filteredFile) 

#removing punctuation to avoid duplicate words
#also lemmatizing some common words
filteredFile = filteredFile.replace("'","")
filteredFile = filteredFile.replace(":", " ")
filteredFile = filteredFile.replace(".", " ")
filteredFile = filteredFile.replace("!", " ")
filteredFile = filteredFile.replace("?", " ")
filteredFile = filteredFile.replace("--", " ")
filteredFile = filteredFile.replace(",", " ")
filteredFile = filteredFile.replace(";", " ")
filteredFile = filteredFile.replace("(", " ")
filteredFile = filteredFile.replace(")", " ")
filteredFile = filteredFile.replace("000", " ")
filteredFile = filteredFile.replace("terrorists", "terrorist ")
filteredFile = filteredFile.replace("americans", "american")
filteredFile = filteredFile.replace("american", "america")

#count characters 
num_chars = len(filteredFile)
#count lines 
num_lines = filteredFile.count('\n')

#DEBUG STATEMENTS
#print(num_chars)
#print(num_lines)
#print(filteredFile)

#split words again
words = filteredFile.split()

#initialize dictionary
d = {}

#if the words exists in the dictionary, add 1 to count. Else, add word to dictionary.
for word in words:
    if word in d:    
        d[word] += 1
    else:
        d[word] = 1
        
#total word count        
num_words = sum(d[word] for word in d)

#create list of top 30 words sorted by word count
lst = [(d[word], word) for word in d]
lst.sort()
lst.reverse()

print('Your input file has characters = ' + str(num_chars))
print('Your input file has num_lines = ' + str(num_lines))
print('Your input file has num_words = ' + str(num_words))
print('\n The 30 most frequent words are \n')

#display top 30 words
i = 1
for count, word in lst[:30]:
    print('%2s.  %4s %s' % (i, count, word))
    i += 1

