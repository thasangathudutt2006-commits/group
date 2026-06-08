for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print()


for i in range(1,9):
    if i%2==0:
        for j in range(1,9):
            if j%2==0:
                print("\u2B1C",end="")
            else:
                print("\u2B1B",end="")
    else:
        for j in range(1,9):
            if j%2==0:
                print("\u2B1B",end="")
            else:
                print("\u2B1C",end="")
    print()
