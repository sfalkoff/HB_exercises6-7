import string

input_file = open('twain.txt') # open/read twain.txt

word_count = {} # creates dict called word_count

# creates list called separate_line of individual words in each line
for line in input_file:
    # remove white space and split line into list of words
    separate_line = line.rstrip().split(" ") 
    # iterates through each word in separate_line list
    for word in separate_line:
        words_with_no_punctuation = ""
        for char in word: # iterate over each character
            separate_chars = char.split()
            if separate_chars[0] in string.punctuation: # if character is punc, remove it 
                del separate_chars[0]
            else:
                words_with_no_punctuation = words_with_no_punctuation + separate_chars[0]
        # turns words to lowercase
        words_with_no_punctuation = words_with_no_punctuation.lower()
        # if lowercase word is not a key in dict, add as key; otherwise add 1 to count
        word_count[words_with_no_punctuation] = word_count.get(words_with_no_punctuation, 0) + 1

for word, count in word_count.iteritems():
    print "%s %s" % (word, count)