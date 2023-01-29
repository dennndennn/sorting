def selection_sort(sort_list):
    for a in range(len(sort_list)):
        lower = min(sort_list[a:])
        index = sort_list.index(lower)
        sort_list[a], sort_list[index] = sort_list[index], sort_list[a]
        print("PASS", a, sort_list)
    print(sort_list)

number_list = []
size = int(input("Enter size of the list \t"))

for i in range(size):
    numbers = int(input("Enter one number to add in the list \t"))
    number_list.append(numbers)

selection_sort(number_list)    