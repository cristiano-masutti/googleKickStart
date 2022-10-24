cases = int(input())

def order():
    elements = int(input())
    cards=[]
    for _ in range(elements):
        cards.append(input())
    check = True
    count = 0
    while check:
        for i in range(1, len(cards)):
            if cards[i] < cards[i-1]:
                cards[i], cards[i-1] = cards[i-1], cards[i]
                count+=1
        check = False
    return count

for case in range(cases):
    swaps = order()
    print("Case #"+str(case+1)+": "+str(swaps))