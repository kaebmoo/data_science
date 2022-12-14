def lengthOfLongestSubstring(s):
    maxLen = 1
    if s == '':
        return 0                      # Dealing with one edge case
    for i in range(len(s)):
        substring = s[i]              # Initialising the substring
        # print(substring)
        for j in range(i+1, len(s)):  # Starting to append characters to substring from i+1
            if s[j] not in substring: # As long as its not repeating. "not in" can be used to check if the character isn't already there in the substring
                substring = substring + s[j]
                print(substring)
                maxLen = max(maxLen, len(substring)) # Updating maxLen if it is greater than the existing maxLen
            else:
                break
    
    
    return maxLen
# abcababcababcab
# abababababab
print(lengthOfLongestSubstring("affedaaffed"))