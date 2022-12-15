# Python program to find maximum contiguous subarray
 
def maxSubArraySum(a):
    size = len(a)
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
 
# Driver function to check the above function
a =  [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is" , maxSubArraySum(a))
 
#This code is contributed by _Devesh Agrawal_