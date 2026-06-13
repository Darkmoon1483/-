7
def reward(box,X,Y):
    win_DEE_Sell =[]
    for l in (box):
        if l >= X and l <=Y :
            win_DEE_Sell.append(l)
    rw = []
    for s in (win_DEE_Sell):
        a = s //100 *2
        rw.append(a)

def display(rw):
    if len(rw) >0:
        print(rw)
    else:
        print("None")
def main():
    n = int(input())
    box = []
    for i in range(n):
        p = float(input())
        box.append(p)
    x,y = input().split()
    X = int(x)
    Y = int(y)
    result = reward(box,X,Y)
    display(result)




if __name__ == "__main__":
    main()