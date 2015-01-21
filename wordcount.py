input_file = open('testfile.txt') # open/read twain.txt

#creates dict called word_count and sets initial count to 1
word_count = {}

# creates list called separate_line of individual words in each line
for line in input_file:
        
    separate_line = line.rstrip()
    separate_line = separate_line.split(" ")

    # iterates through each word in separate_line list
    for word in separate_line:
        # turns words to camelcase
        word = word.capitalize()
        # if camelcase word is not a key in dict, add it to the dict
        if word not in word_count.keys():
            word_count[word] = 1 # adds as a key with value 1
        # adds 1 to value for each time word
        else:
            word_count[word] = word_count[word] + 1 

for word, count in word_count.iteritems():
    print "%s %s" % (word, count)