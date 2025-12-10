len = int(input("Enter the length of the List : "))
lst = []

for i in range(len):
    element = int(input(f"Enter the integer element{i+1} : "))
    lst.append(element)

print("The List is : ",lst)

total = sum(lst)
print("Sum of List Elements is : ",total)