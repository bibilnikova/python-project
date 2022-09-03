words = []
with open('text.txt', 'r') as r:
    for line in r:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
top5 = counts.most_common(5)
print(top5)