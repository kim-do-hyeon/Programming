def insertion_sort(unsoroted_list):
    j = 1
    for j in range(j, len(unsoroted_list)):
        key = unsoroted_list[j]
        i = j - 1
        while i >= 0 and unsoroted_list[i] > key:
            unsoroted_list[i + 1] = unsoroted_list[i]
            i = i - 1
        unsoroted_list[i + 1] = key
        print(' '.join(unsoroted_list))

    return unsoroted_list
num = int(input())
unsoroted_list = input().split(' ')
sorted_list = insertion_sort(unsoroted_list)