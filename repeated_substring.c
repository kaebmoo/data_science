// A C++ program to check if a string is 'n' times
// repetition of one of its substrings
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

char *string_repeat(const char *s, int n);
void computeLPSArray(char str[], int M, int lps[]);
bool isRepeat(char str[]);

char *string_repeat(const char *s, int n)
{
  size_t slen = strlen(s);
  char *dest = (char *) malloc(n*slen+1);

  int i;
  char *p;

  for (i=0, p=dest; i<n; ++i, p+= slen) {
    memcpy(p, s, slen);
  }
  *p = '\0';

  return dest;
}
  
// A utility function to fill lps[] or compute prefix
// function used in KMP string matching algorithm. Refer
// https://www.geeksforgeeks.org/archives/11902 for
// details
void computeLPSArray(char str[], int M, int lps[])
{
    // length of the previous longest prefix suffix
    int len = 0;
    int i;
  
    lps[0] = 0; // lps[0] is always 0
    i = 1;
  
    // the loop calculates lps[i] for i = 1 to M-1
    while (i < M) {
        if (str[i] == str[len]) {
            len++;
            lps[i] = len;
            i++;
        }
        else // (pat[i] != pat[len])
        {
            if (len != 0) {
                // This is tricky. Consider the example
                // AAACAAAA and i = 7.
                len = lps[len - 1];
  
                // Also, note that we do not increment i
                // here
            }
            else // if (len == 0)
            {
                lps[i] = 0;
                i++;
            }
        }
    }
}
  
// Returns true if str is repetition of one of its
// substrings else return false.
bool isRepeat(char str[])
{
    bool flag;
    int ix;
    char *res, *cp;
    // Find length of string and create an array to
    // store lps values used in KMP
    int n = strlen(str);
    int lps[n];
    

    res = (char *) malloc(n+1);
    cp = (char *) malloc(n+1);
    memset(res, '\0', n+1);
    memset(cp, '\0', n+1);
  
    // Preprocess the pattern (calculate lps[] array)
    computeLPSArray(str, n, lps);
  
    // Find length of longest suffix which is also
    // prefix of str.
    int len = lps[n - 1];
  
    // If there exist a suffix which is also prefix AND
    // Length of the remaining substring divides total
    // length, then str[0..n-len-1] is the substring that
    // repeats n/(n-len) times (Readers can print substring
    // and value of n/(n-len) for more clarity.

    // debug
    //printf("%d ", n/(n-len));
    int repeat = n/(n-len) / 2;
    //printf("%d ", repeat);
    for (ix=0; ix<=strlen(str)-len-1;ix++) {
        // printf("%c", str[ix]);
        cp[ix] = str[ix];
    }
    cp[ix] = '\0';
    printf(" ");
    // end debug
    flag = (len > 0 && n % (n - len) == 0);
    if (flag) {
        res = string_repeat(cp, repeat);
    }
    else {
        strcpy(res, "-1");
    }
    printf("%s ", res);
    return(flag);
    //return (len > 0 && n % (n - len) == 0) ? true : false;
}
  
// Driver program to test above function
int main()
{
    char txt[][100]
        = { "ABCABC",        "ABABAB",   "ABCDABCD",
            "GEEKSFORGEEKS", "GEEKGEEKGEEKGEEK", "AAAACAAAAC",
            "ABCDABC", "abababababab", "abcababcababcab" };
    int n = sizeof(txt) / sizeof(txt[0]);
    for (int i = 0; i < n; i++)
        isRepeat(txt[i]) ? printf("True\n")
                         : printf("False\n");
    return 0;
}
  
// This code is contributed by Aditya Kumar (adityakumar129)