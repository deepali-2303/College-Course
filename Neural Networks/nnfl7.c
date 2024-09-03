#include <stdio.h>

int main()
{

  int A[1][15] = {{-1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1}};
  int B[1][15] = {{1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1}};
  int C[1][15] = {{1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1}};
  int D[1][15] = {{1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1}};
  int E[1][15] = {{1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1}};

  int patterns[5][15];

  for (int i = 0; i < 15; i++)
  {
    patterns[0][i] = A[0][i];
    patterns[1][i] = B[0][i];
    patterns[2][i] = C[0][i];
    patterns[3][i] = D[0][i];
    patterns[4][i] = E[0][i];
  }

  int transpose[15][5];

  for (int i = 0; i < 15; i++)
  {
    for (int j = 0; j < 5; j++)
    {
      transpose[j][i] = patterns[i][j];
    }
  }
  
  // for (int i = 0; i < 5; i++)
  // {
  //   for (int j = 0; j < 15; j++)
  //   {
  //     printf("%d ", patterns[i][j]);
  //   }
  //   printf("\n");
  // }
  return 0;
}