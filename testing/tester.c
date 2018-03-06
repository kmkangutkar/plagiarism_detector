#include <stdio.h>

int min(int x, int y){
	if (x < y){
		return x;	
	}else{
		return y;	
	}		
}

int main(){
	int a1, b2, c1;
	printf("Enter 2 integers: ");
	scanf("%d%d", &a1, &b2);
	c1 = min (a1,b2);
	printf("Smaller = %d", c1);
	if(c1 == a1){
		printf("muhahah!");
	}
	for (int i = 0; i < 10; i++){
		a1 = 2;
	}
	return 0;	
}

