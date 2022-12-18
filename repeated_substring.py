# Python3 code to demonstrate working of
# Check if string repeats itself
# Using List comprehension + Brute Force
  
# initializing string 
test_str = "GeeksforGeeksGeeksforGeeksGeeksforGeeks"
# test_str = "abcababcababcab"
test_str = "abcxabc"
test_str = "acbdfghybdf"
test_str = "abababababab"
test_str = "GEEKGEEKGEEKGEEK"
  
# printing original string 
print("The original string is : " + test_str)
  
# using List comprehension + Brute Force
# Check if string repeats itself
res = None
print(len(test_str)//2 + 1)
print()
for i in range(1, len(test_str)//2 + 1):
    if (not len(test_str) % len(test_str[0:i]) and test_str[0:i] *
           (len(test_str)//len(test_str[0:i])) == test_str):
        res = test_str[0:i]
  
# printing result
if res != None:
    print("The root substring of string : " + res)
else:
    print("None")