#Day 2
def rotate(a, n, k):
    k = k % n

    for i in range(0, n):
        if(i < k):
            print(a[n + i - k], end = ", ")
        else:
            print(a[i - k], end = ", ")
    print("\n")
nums = [1,2,3,4,5,6,7]
K = 3
N = len(nums)

rotate(nums, N, K)