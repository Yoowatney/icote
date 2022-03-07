#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int n;

	// printf("%d\n", scanf("%d", &n));
	// exit(0);
	n = 3;
	for (int i = 0; i < n; i++)
	{
		printf("n : %d\n", n);
		scanf("%d", &n);
	}
	return 0;
}
