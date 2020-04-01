text = []
for i in range(200):
    temp = input()
    if(temp == 'END'):
        break
    else:
        text.append(temp)
list_count = len(text)

result = []
for i in range(list_count):
    temp = text[i].split()
    result.append(temp)
# print(result)

w_count = {}
for i in range(1):
    for test in result[i]:
        try :
            w_count[test] += 1
        except :
            w_count[test] = 1
    print('\n')
# from collections import Counter
# wordDict = Counter()

# for i in range (list_count):
#     for word in result[i]:
#         try :
#             wordDict[word] += 1
#         except :
#             wordDict[word] = 1

# for word, freq in wordDict.most_common(5):
#     print(word,':', freq)

res = sorted(w_count.items())
print(res)
