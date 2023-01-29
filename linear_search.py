number_list = []

size = int(input("Enter size of the list \t"))
for i in range(size):
    numbers = int(input("Enter one number to add in the list \t"))
    number_list.append(numbers)

# found = False    

num = int(input("Enter a number to search \t"))

for i in range(len(number_list)):
    if num == number_list[i]:
        found = True
        print ("\n%d Fount at position %d" % (num, i))
        break

if not found:
    print ("not in the list")    