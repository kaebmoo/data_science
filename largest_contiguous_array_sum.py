# [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]

from sys import maxsize
 
# Function to find the maximum contiguous subarray
# and print its starting and end index
def maxSubArraySum(a,size):
 
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0,size):
 
        max_ending_here += a[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
 
    print ("Maximum contiguous sum is %d"%(max_so_far))
    print ("Starting Index %d"%(start))
    print ("Ending Index %d"%(end))
 
# Driver program to test maxSubArraySum
a =  [-13, 3, 1, -1]
maxSubArraySum(a,len(a))