#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int test()
{
	usleep(100000);
	return 100;
}
int main(int argc, char *argv[])
{
	int n;

	n = 3;
	for (int i = 0; i < test(); i++)
	{
		printf("Hi!!\n");
	}
	return 0;
}
