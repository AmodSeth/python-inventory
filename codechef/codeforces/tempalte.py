import sys
import threading
def solve():
    n = int(input())
    b = list(map(int, input().split()))
 
    # ---- solve one test case here ----
    b.sort()
    total = 0
    other = 0
    for i in range(len(b)):
        if b[i] > 0:
            total = max(total, len(b) - i)
            # print("TOTAL:", total)
            other += (b[i] - 1)
    if other >= n - 1:
        print(total)
    else:
        print(total - (n - 1 - other))
 
 
def main():
    input = sys.stdin.readline
 
    t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()
