def maximumSubarraySum(arr):
    n = len(arr)
    maxSum = -1e8

    for i in range(0, n):
        currSum = 0
        for j in range(i, n):
            currSum = currSum + arr[j]
            if(currSum > maxSum):
                maxSum = currSum

    return maxSum

if __name__ == "__main__":
    # Your code goes here
    a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7];
    # a = [1, -2, 0, 3]
    print(maximumSubarraySum(a));