/*level 3*/

#include <stdio.h>

#define FALSE 0
#define UNUSED 4
#define ALWAYS_TRUE 1
#define SIZE 8190
char prime[8191];

main(){
	int i, primes, k, counter, iteration;
	
	printf("10 iterations/n");
	for(iteration = 1; iteration <= 10; iteration++){
		counter=0;
		for(i = 0; i <= SIZE; i++){
			prime[i] = ALWAYS_TRUE;	
		}
		for(i = 0; i <=SIZE; i++){
			if(prime[i]){
				primes = i+i+3;
				for (k = i + primes; k < SIZE; k += primes)
					prime[k] = FALSE;
				counter++;
			}
		}
	}
	printf("%d %d\n", primes, counter);
}
