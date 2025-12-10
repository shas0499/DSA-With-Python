len = int(input("Enter the length of the List : "))
lst = []

for i in range(len):
    element = int(input(f"Enter the integer element{i+1} : "))
    lst.append(element)

print("The List is : ",lst)

print("Minimum is : ",min(lst))
print("maximum is : ",max(lst))