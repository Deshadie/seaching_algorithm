import random
import string
import math
import psutil
from timeit import default_timer as execute_time

list1_text = []
list2_text = []
list3_text = []

for i in range(0, 1000):
    list1_text.append(''.join(random.sample(string.ascii_lowercase, 4)))
for i in range(0, 10000):
    list2_text.append(''.join(random.sample(string.ascii_lowercase, 4)))
for i in range(0, 100000):
    list3_text.append(''.join(random.sample(string.ascii_lowercase, 4)))

list1_text_sorted = sorted(list1_text)
list2_text_sorted = sorted(list2_text)
list3_text_sorted = sorted(list3_text)


# ---------------for linear search------------------------>


def linear_search_s(list_linear_s, key):
    for s in range(len(list_linear_s)):
        if list_linear_s[s] == key:
            return s
    return -1


def linear_search_display_s(test_linear_s):
    if test_linear_s == -1:
        print("(linear search_string)Element not found")
    else:
        print("(linear search_string)Key element is found at index :", test_linear_s)


# linear_search_display_s(linear_search_s(list1_text, list1_text[100]))
# linear_search_display_s(linear_search_s(list1_text_sorted, list1_text_sorted[100]))

# ---------------linear search end------------------------>

# ---------------for binary search-------only use for sorted list--------------------->


def binary_search_s(list_binary, k, left, right):
    while right >= left:
        mid = left + (right - left) // 2
        if list_binary[mid] == k:
            return mid
        elif list_binary[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_display_s(test_binary):
    if test_binary == -1:
        print("(binary search string-Element not found")
    else:
        print("binary search string-Key element is found at index :", test_binary)


# binary_search_display_s(binary_search_s(list1_text_sorted, 'ughk', 0, len(list1_text_sorted) - 1))

# ---------------Binary search end------------------------>

# ----------------For Jump search------only use for sorted list---------------------->

def jump_search(jump_list, search_jump):
    low = 0
    m = int(math.sqrt(len(jump_list)))

    for j in range(0, len(jump_list), m):
        if jump_list[j] < search_jump:
            low = j
        elif jump_list[j] == search_jump:
            return j
        else:
            break

    c = low
    for j in jump_list[low:]:
        if j == search_jump:
            return c
        c = c+1
    return -1


def jump_search_display(test_jump):
    if test_jump == -1:
        print("Jump search string-Not found")
    else:
        print("Jump search string-Key element is found at index :", test_jump)


# jump_search_display(jump_search(list1_text_sorted, 'wefg'))

# ---------------Jump search end------------------------>

# ---------------for Exponential Search-------only use for sorted list------------>


def exponential_search(list_binary, k):
    n = len(list_binary)

    if list_binary[0] == k:
        return 0
    e = 1  # ----------->e=index
    while e < n and list_binary[e] <= k:
        e = e * 2

    return binary_search_s(list_binary, k, e // 2, min(e, n))


def exponential_search_display(test_expo):
    if test_expo == -1:
        print("(Exponential Search_string)Element not found in the list ")
    else:
        print("(Exponential Search_string)Element is present at index %d" % test_expo)


# exponential_search_display(exponential_search(list1_text_sorted, 'jhgf'))


# ---------------End Exponential Search------------------->

print('----------------------------------------Result Analysis-------------------------------------------------\n')
print('----------Linear Search String Sorted -----------------')
start = execute_time()
linear_search_display_s(linear_search_s(list1_text_sorted, 'hdst'))
end = execute_time()
print("* Time for 1000 data set :", round((end - start) * 1000, 5), "ms\n")

start = execute_time()
linear_search_display_s(linear_search_s(list2_text_sorted, 'hdst'))
end = execute_time()
print("* Time for 10000 data set :", round((end - start) * 1000, 5), "ms\n")

start = execute_time()
linear_search_display_s(linear_search_s(list2_text_sorted, 'hdst'))
end = execute_time()
print("* Time for 100000 data set :", round((end - start) * 1000, 5), "ms\n")