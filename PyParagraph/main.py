# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Module for regex
import re

# Get Current working directory of main.py file
cwd = os.getcwd()

# Set path for file: assign paragraph_1.txt or paragraph_2.txt in below line

csvpath = os.path.join(cwd, "raw_data", "paragraph_1.txt")
csvpath = os.path.normcase(csvpath)
csvpath = os.path.normpath(csvpath)

paragraph_output_file = os.path.join(cwd, "output","output_1.csv")
paragraph_output_file = os.path.normcase(paragraph_output_file )
paragraph_output_file = os.path.normpath(paragraph_output_file )

# Read file into a string variable
with open(csvpath,'r', newline="") as text:
    paragraph = text.read()

sentences = re.split("(?<=[.!?]) +", paragraph)

# Count number of words
count_words = 0
for s in sentences:
    count_words += len(re.findall(r'\w+', str(s)) ) 

# Count number of sentences

count_sentences = len(sentences)

# Split paragraph into characters, count number of letters and average letters per word and store it till decimal
avg_letters_per_word = float('%.1f'%(len([letter for letter in paragraph if letter.isalpha()])/count_words))

# Calculate average sentence length in words
avg_sentence_length = 0.0
if count_sentences > 0:
    avg_sentence_length = float('%.1f'%(count_words/count_sentences))

# Assign Paragraph statictics names to Column Headers
paragraph_analysis_col_header = [ "Paragraph Analysis",
                                  "-----------------",
                                  "Approximate Word Count:",
                                  "Approximate Sentence Count:",
                                  "Average Letter Count:",
                                  "Average Sentence Length:"
                                  ]

# Assign total votes cast results values into voting results list variable
paragraph_analysis_col_results = [   "",
                                     "",
                                     count_words,
                                     count_sentences,
                                     avg_letters_per_word,
                                     avg_sentence_length
                                 ]

# Zip two lists together into tuples for writing to file
paragraph_results_file = list(zip(paragraph_analysis_col_header, paragraph_analysis_col_results))

# Writing to file
with open(paragraph_output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # print out to file:
    for i, j in paragraph_results_file:
        print(i, j, end='\n', file=datafile)
