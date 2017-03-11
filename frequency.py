""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string

def get_line_list(file_name):
    """ Gets the specified document.  Header and footer comments are stripped away.  
    Returns a list that contains the lines of the documents as split in the
    document
    """
    f = open(file_name, 'r') # Opens file passed into the  function
    lines = f.readlines() # MAkes a list that contains every line
    curr_line = 0 # Start at the beginning of the document
    flag = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        #Look for given string, move to next line
      curr_line += 1
      flag = 1
    end_line = curr_line+1
    while "Project Gutenberg" not in lines[end_line]: #check for footer
        end_line += 1
    if flag == 1: #Check if it found the header
        lines = lines[curr_line+1:end_line] #Get rid of everything before the start of the book
    return lines

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    line_list = get_line_list(file_name)
    list_of_words = []
    for line in line_list:
        stripped_line = line.strip(string.punctuation)
        lower_line = line.lower()
        words_in_line = lower_line.split()
        list_of_words.extend(words_in_line)
    return list_of_words


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_counts = {}
    for word in word_list:
        count = word_counts.get(word,0)
        word_counts[word] = count+1
    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
    top_n = ordered_by_frequency[:n]
    return top_n

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    words = get_word_list("AliceInWonderland.txt")
    ordered = get_top_n_words(words,100)
    print(ordered)