temp = input().upper()
unique = list(set(temp))

cnt_list = []

for i in unique :
    cnt = temp.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print("?")
else :
    max_index = cnt_list.index(max(cnt_list))
    print(unique[max_index])