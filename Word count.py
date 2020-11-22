file = open("C:\\Users\szere\OneDrive\Pulpit\kody Python\word coutning.txt", "r+")

wordcount = {}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] = wordcount[word] + 1
for word, occurence in wordcount.items():
    print(word, occurence)
