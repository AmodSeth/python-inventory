# his weight is tripled after every year, while Bob's weight is doubled after every year


def solve():
    a , b = map(int, input().split())
    count = 0
    while True:
        a *=3
        b *=2
        count +=1
        if a > b:
            print(count)
            return 
        



solve()