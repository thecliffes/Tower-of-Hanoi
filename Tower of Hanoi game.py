def stack(sname):
    stack=[]
    for num in range(sname-1, -1, -1):
        stack.append(num+1)
    return stack


astack = stack(4)
bstack = []
cstack = []
winningstack = astack.copy()


def showstacks():
    print(astack)
    print(bstack)
    print(cstack)


def move():
    emptystack = []

    while True:
        print("\nWhich stack to move from?\n1..2..3..")
        startstack = input()
        if startstack == "1" and len(astack) != 0:
            emptystack.append(astack[-1])
            astack.pop()
            break
        elif startstack == "2" and len(bstack) != 0:
            emptystack.append(bstack[-1])
            bstack.pop()
            break
        elif startstack == "3" and len(cstack) != 0:
            emptystack.append(cstack[-1])
            cstack.pop()
            break
        else:
            print("\nGive a valid value")

    while True:
        print("\nWhich stack to move to?\n1..2..3..")
        endstack = input()
        if endstack == "1" and (len(astack) == 0 or (astack[-1]) >= emptystack[0]):
            astack.append(emptystack[0])
            emptystack.clear()
            break
        elif endstack == "2" and (len(bstack) == 0 or (bstack[-1]) >= emptystack[0]):
            bstack.append(emptystack[0])
            emptystack.clear()
            break
        elif endstack == "3" and (len(cstack) == 0 or (cstack[-1]) >= emptystack[0]):
            cstack.append(emptystack[0])
            emptystack.clear()
            break
        else:
            print("Give a valid value")


while True:
    if winningstack == cstack or winningstack == bstack:
        print("\nWinner winner chicken dinner!")
        break
    else:
        move()
        showstacks()
