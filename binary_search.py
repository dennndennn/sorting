
def binary_search(sorted_list, length, key):
    lower = 0
    high = length -1
    while lower <= high:
        mid = (lower + high) // 2
        if key == sorted_list[mid]:
            print("Enter number %d is present at position: %d" % (key, mid))
            return -1
        elif key < sorted_list[mid]:
            high = mid -1
        elif key > sorted_list[mid]:
            lower = mid + 1
    print("Number not Found") 
    return -1           

number_list = []
size = int(input("Enter size of the list \t"))
for i in range(size):
    numbers = int(input("Enter one random number to add in the list\t"))
    number_list.append(numbers)

number_list.sort()
print("The list will be sorted, the sorted list is", number_list)

num = int(input("Enter a number to search \t"))

binary_search(number_list, size, num)


