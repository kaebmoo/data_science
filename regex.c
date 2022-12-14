#include <stdio.h>
#include <string.h>
#include <regex.h>

void SearchingChallenge(char * str) {
  
  // code goes here  
  regex_t regex;
  int retx;

  retx = regcomp(&regex, "^[A-Za-z][A-Za-z0-9]*(?:_+[A-za-z0-9]+)*$", 0);
  if (retx) {
    fprintf(stderr, "Could not compile regex\n");
  }
  printf("%d\n", retx);
  // retx = regexec(&regex, &str, 0, NULL, 0);
  if (!retx) {
    strcpy(str, "true");
  }
  else if (retx == REG_NOMATCH) {
    strcpy(str, "false");
  }

  printf("%s", str);

}

int main(void) {
    regex_t regex;
    int retx;

    retx = regcomp(&regex, "^[A-Za-z][A-Za-z0-9]*(?:_+[A-Za-z0-9]+)*$", 0);
    printf("%d\n", retx);


    return 0;
}