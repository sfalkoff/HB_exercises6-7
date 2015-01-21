input_file = open('twain.txt') # open/read twain.txt

word_count = {}
# creates list of individual words in each line
for line in input_file:
    separate_line = line.rstrip()
    separate_line = separate_line.split(" ")
    count = 1
    for word in separate_line:
        if word not in word_count.keys():
            word_count[word] = count # adds as a key with value 1
        else:
            word_count[word] = (count + 1) # adds 1 to value for each time word appears as a key

print word_count
