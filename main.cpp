#include <stdio.h>
#include <stdlib.h>
#include <time.h>

main() {
	int num, i,a;
    	srand(time(NULL));
	
    	num = rand();
    	num = num % 100;
	
	printf("In order to find the number, please enter your guess.\n");
	scanf("%d",&a);
	do{
		if(num>a) {
			printf("Enter a larger number.\n");
			scanf("%d",&a);
		}
		else {
			printf("Enter a smaller number.\n");
			scanf("%d",&a);
		}
	} while(a!=num);
	if(num==a)
		printf("Found it: %d",num);
	return 0;
}
