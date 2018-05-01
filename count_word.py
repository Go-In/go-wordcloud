import deepcut

# captions = open('caption.txt', 'r')
# captions = open('caption_bnk.txt', 'r')
captions = open('caption_sweat.txt', 'r')

collecting = {'test': 0}

for line in captions:
    words = deepcut.tokenize(line)
    for word in words: 
        if word not in collecting:
            collecting[word] = 1
        else:
            collecting[word] += 1

print(collecting)
