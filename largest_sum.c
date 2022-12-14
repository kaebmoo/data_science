#include <stdio.h> 
#include <string.h>
#include <stdint.h>
#include <limits.h>


void ArrayChallenge(int arr[], int arrLength) {
  
  // code goes here  
  // printf("0x%jx\n", (uintmax_t)SIZE_MAX);
  int maxSum = INT_MIN;
  //printf("%d\n", maxSum);
  int currSum = 0;
  int i, j;

  for (i = 0; i < arrLength; i++) {
    currSum = 0;
    for (j = i; j < arrLength; j++) {
      currSum = currSum + arr[j];
      if (currSum > maxSum)
        maxSum = currSum;
    }
  }
  arr[0] = maxSum;
  printf("%d", arr[0]);

}

int main(void) { 
   
  // keep this function call here
  int A[] = {-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7};
  int arrLength = sizeof(A) / sizeof(*A);
  ArrayChallenge(A, arrLength);
  return 0;
    
}