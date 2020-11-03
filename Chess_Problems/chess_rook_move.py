import time

def rook_move(sletter, snum):
    #print(sletter, snum)
    dletter = int(input("\nPlease enter a destination X coordinate: "))
    dnum = int(input("Please enter a destination Y coordinate: "))

    #print(dletter, dnum)

    if dletter > 8:
        raise ValueError("\nPlease keep the number in a range of 1-8".upper())
    elif dletter <= 0:
        print("Please keep the number in a range of 1-8")
    elif dnum > 8:
        print("Please keep the number in a range of 1-8")
    elif dnum <= 0:
        print("Please keep the number in a range of 1-8")
    elif sletter == dletter:
        print("YES")
    elif snum == dnum:
        print("YES")
    else:
        print("NO")

while True:
    sletter = int(input("\nPlease enter a starting X coordinate: "))
    snum = int(input("Please enter a starting Y coordinate: "))

    if sletter > 0 and sletter <= 8 and snum > 0 and snum <= 8:
        rook_move(sletter, snum)
