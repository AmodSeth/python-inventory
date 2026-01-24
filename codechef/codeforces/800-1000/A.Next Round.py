def solve():
    n , position = map(int, input().split())
    arr = list(map(int, input().split()))

    score = arr[position-1]
    count = 0
    for _ in arr:
        if _ >= score and _ > 0:
            count += 1
        
    print(count)

            
    





solve()