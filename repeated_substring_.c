#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

char * string_repeat(const char *s, int n);
void computeLPSArray(char str[], int M, int lps[]);
char *isRepeat(char str[]);

char *isRepeat(char str[])
{
  bool flag;
  int ix;
  char *res, *cp;

  int n = strlen(str);
  // int lps[n];
  int *lps;
  lps = malloc(n * sizeof(int));

  res = (char *) malloc(n+1);
  cp = (char *) malloc(n+1);
  memset(res, '\0', n+1);
  memset(cp, '\0', n+1);

  computeLPSArray(str, n, lps);
  int len = lps[n-1];

  int repeat = n/(n-len) / 2;
  for (ix = 0; ix <= strlen(str)-len-1; ix++) {
    cp[ix] = str[ix];
  }
  cp[ix] = '\0';
  flag = (len > 0 && n % (n - len) == 0);
  if (flag) {
    res = string_repeat(cp, repeat);
  }
  else {
    strcpy(res, "-1");
  }

  free(lps);
  return(res);
  // return (len > 0 && n % (n - len) == 0) ? true : false;
}

void computeLPSArray(char str[], int M, int lps[]) 
{
  int len = 0;
  int i;

  lps[0] = 0;
  i = 1;

  while(i < M) {
    if (str[i] == str[len]) {
      len++;
      lps[i] = len;
      i++;
    }
    else {
      if (len != 0) {
        len = lps[len - 1];
      }
      else {
        lps[i] = 0;
        i++;
      }
    }
  }
}

void MathChallenge(char * str) {

  // code goes here  
  str = isRepeat(str);
  printf("%s\n", str);

}

char * string_repeat(const char *s, int n)
{
  size_t slen = strlen(s);
  char *dest = malloc(n*slen+1);

  int i;
  char *p;

  for (i=0, p=dest; i<n; ++i, p+= slen) {
    memcpy(p, s, slen);
  }
  *p = '\0';

  return dest;
}

int main(void) { 
   
  // keep this function call here
  MathChallenge("abababababab");
  MathChallenge("GEEKGEEKGEEKGEEK");
  return 0;
    
}