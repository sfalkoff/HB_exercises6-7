input_file = open('twain.txt') # open/read twain.txt

# creates dict called word_count and sets initial count to 1
word_count = {}

# creates list called separate_line of individual words in each line
for line in input_file:
    # remove white space and split line into list of words
    separate_line = line.rstrip().split(" ")
    # iterates through each word in separate_line list
    for word in separate_line:
        # turns words to lowercase
        word = word.lower()
        # if lowercase word is not a key in dict, add as key; otherwise add 1 to count
        word_count[word] = word_count.get(word, 0) + 1 

for word, count in word_count.iteritems():
    print "%s %s" % (word, count)