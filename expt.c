#include <stdio.h>

/**
 * 求a的n次方
 *
 * 算法复杂度 以2为底的n的对数
 */
int expt(unsigned int a, unsigned int n)
{
  unsigned int res = 1;
  unsigned int acc = n & 1;

  while (n) {
    if (acc) {
      res *= a;
    }
    a *= a;
    n >>= 1;
    acc = n & 1;
  }

  return res;
}

int main()
{
  printf("2 ^ 3 = %d\n", expt(2, 3));
  printf("3 ^ 4 = %d\n", expt(3, 4));
  return 0;
}
