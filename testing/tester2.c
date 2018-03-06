#include <stdio.h>

void print (char* str){
	printf("%s", str);
}
void enter(int a){
	printf("%d", a);
}

int main(){
	int p;
	int q;
	int r;
	printf("Enter 2 integers: ");
	scanf("%d%d", &p, &q);
	if (p < q){
		r = p;
	}else{
		r = q;
	}
	printf("Smaller = %d", r);
	if(r == p){
		print("muhahah");
	}
	int i = 0;
	while(i < 10){
		p = 2;
		i++;
	}
	return 0;	
}

