#include <stdlib.h>
#include <stdio.h>




int main(int argc, char * argv[])
{
	if(argc<2)
{
fprintf(stderr,"Incorrect Usage\n");
return EXIT_FAILURE;
}
	long int seedval = atoi(argv[1]);
	srand48(seedval);
	for(int i = 0; i< 10; i++)
{
	double res = drand48();
	printf("Results from drand48(): %g\n",res);
}
}
