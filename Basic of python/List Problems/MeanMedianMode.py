import numpy as np
import statistics

len = int(input("Enter the length of the List : "))
lst = []

for i in range(len):
    element = int(input(f"Enter the integer element{i+1} : "))
    lst.append(element)

print("The List is : ",lst)

print("Mean : ",np.mean(lst))
print("Median : ",np.median(lst))
print("Mode : ",statistics.mode(lst))