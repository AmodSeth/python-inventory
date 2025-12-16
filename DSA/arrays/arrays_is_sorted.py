nums = [10, 20, 30, 40, 50]

def isSorted(self, arr) -> bool:
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            return False
        return True



if __name__ == "__main__":
