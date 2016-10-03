def words_in_poem(filename):
    word_counts = {}
    with open(filename) as input_poem:
        for line in input_poem:
            words = line.strip().split()
            for word in words:
                # word_counts[word] = word_counts.get(word, 0) + 1
                ## line 8 reassigns word_counts[word] with every iteration
                ## lines 11-14 increment word_counts[word] with every iteration
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    for word, count in word_counts.items():
        # # word_counts.items() returns a list of tuples
        # print "%s %d" % (word, count)
        # # line 16 produces same result as line 18
        print word, count

words_in_poem("test.txt")
# words_in_poem("twain.txt")
