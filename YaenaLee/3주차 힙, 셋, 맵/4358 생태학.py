from collections import defaultdict
import sys
dictionary = defaultdict(int)
while(True):
    name = sys.stdin.readline().strip()
    dictionary[name] += 1
    # print(dictionary)
    if not name:
        break


# print(total)
dictionary = dict(sorted(dictionary.items())[1:])
total = sum(dictionary.values())
for i in dictionary:
    print(i, "{:.4f}".format(dictionary[i]/total*100))
