#python3
numbers_of_elements = int(input())
num_list = [int(element) for element in input().split()]

first_max_index = 0
first_max = 0
for index, element in enumerate(num_list):
    if first_max < element:
        first_max = element
        first_max_index = index

next_max = 0
next_max_index = 0
for index, element in enumerate(num_list):
    if next_max < element and first_max_index != index:
        next_max = element
        next_max_index = index

print(num_list[first_max_index] * num_list[next_max_index])
