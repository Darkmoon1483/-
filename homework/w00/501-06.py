def cBF(W, L, T):
    broadFoot = int( W/2.5*L/2.5*T/2.5/144)
    return(broadFoot)

def setGrade(BF):
    if BF <= 10 :
        grade = "A"
    elif BF <= 30:
        grade = "B"
    else:
        grade = "C"
    return grade

def main():
    W, L, T = input().split() #page1
    W1 = int(W)
    BF1 = cBF(W1, int(L), float(T))
    grade1 = setGrade(BF1)
    W, L, T = input().split() #page2
    W2 = int(W)
    BF2 = cBF(W2, int(L), float(T))
    grade2 = setGrade(BF2)

    if grade1 == grade2:
        print("Y")
    else:
        print("N")
    print(f"{BF1} {grade1}")
    print(f"{BF2} {grade2}")