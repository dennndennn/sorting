def bubble_sort(sort_list):
    for a in range (len(sort_list)):
        for b in range (len(sort_list) -1):
            if sort_list[b] > sort_list[b+1]:
                sort_list[b], sort_list[b+1] = sort_list[b+1], sort_list[b]

    print(sort_list)

number_list = []
size = int(input("Enter size of the list \t"))

for i in range(size):
    numbers = int(input("Enter one number to add in the list \t"))
    number_list.append(numbers)

bubble_sort(number_list)    