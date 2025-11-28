myVar = 10

def func():
    global myVar    # Call the global variable before modify the value
    #myVar = 7
    myVar += 1  # Can't Modify without initialize.
    print(myVar)

func()
print(myVar)