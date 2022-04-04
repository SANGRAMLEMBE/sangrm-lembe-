# sangrm-lembe-
swapping  with 2 variable in c lang.
#include<stdio.h>
#include<conio.h>
void main()
{
int a,b;
clrscr();
a = 14;
b = 8;
printf("\n a=%d",a);
printf("\n b = %d",b);
a=a+b;
b=a-b;
a=a-b;
printf("\n after swapping ");
printf("\n A=%d",a);
printf("\n b=%d",b);
getch();
}
