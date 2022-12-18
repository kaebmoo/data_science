/* code from chatgpt but wrong answer */
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
    // initializing string
    char test_str[] = "GEEKGEEKGEEKGEEK";
    // test_str = "abcababcababcab"
    // test_str = "abcxabc"
    // test_str = "acbdfghybdf"
    // test_str = "abababababab"
    // test_str = "GeeksforGeeksGeeksforGeeksGeeksforGeeks"
    int i;

    // printing original string
    printf("The original string is: %s\n", test_str);

    // using brute force
    // check if string repeats itself
    char* res = NULL;
    int len = strlen(test_str);
    for (i = 1; i <= len / 2; i++)
    {
        if (len % i) continue;

        bool found = true;
        for (int j = 0; j < i; j++)
        {
            for (int k = j + i; k < len; k += i)
            {
                if (test_str[j] != test_str[k])
                {
                    found = false;
                    break;
                }
            }
            if (!found) break;
        }

        if (found)
        {
            res = test_str;
            break;
        }
    }

    // printing result
    if (res != NULL)
    {
        printf("The root substring of string: %.*s\n", i, res);
    }
    else
    {
        printf("None\n");
    }

    return 0;
}
