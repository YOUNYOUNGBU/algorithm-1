def binary_search(A, target):
    start = 0
    end = len(A) - 1
    found = False

    while start <= end:
        mid = (start + end) // 2
        midv = A[mid]

        if midv > target:
            end = mid - 1
        elif midv < target:
            start = mid + 1
        else:
            found = True
            break
    return 1 if found else 0

N = int(input())
A = list(map(int, input().split()))
A.sort

M = int(input())
target_list = list(map(int, input().split()))

for target in target_list:
    print(binary_search(A, target))