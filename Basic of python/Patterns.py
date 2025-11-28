# m row and n coulmn

row = int(input("Enter the row number : "))
coulumn = int(input("Enter the column number : "))

for i in range(1,row+1):
    for i in range(1,coulumn+1):
        print(i, end=" ")
    print("")

print("------------------------")
# 1
# 1 2
# 1 2 3

for i in range(1,row+1):
    for j in range(1,row+1):
        if j<=i:
            print(j,end=" ")
        else:
            break
    print("")

print("------------------------")

#       *
#    *  *
# *  *  *
for i in range(1,row+1):
    for j in range(1,row+1):
        if j <= row-i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("")

print("------------------------")