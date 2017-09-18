import operator
import re

myFile = open('/home/utku/Github/blog-posts/linear-regression/linear-regression.md', 'r')
words = myFile.read().lower().split(' ')
dictionary = {}

for word in words:
    word = re.sub('\W+', '', word)          # remove non-alpha-numeric characters

    if len(word) > 1 and len(word) < 20:    # don't allow too short and too long words
        dictionary[word] = dictionary[word] + 1 if word in dictionary else 1

for k, v in sorted(dictionary.items(), key=operator.itemgetter(1)):
    print(k, v)
