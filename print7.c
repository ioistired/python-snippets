#include <stdio.h>
char array[30000] = {0};
char *ptr=array;
int main(void) {
++*ptr;
++*ptr;

++ptr;

++*ptr;
++*ptr;
++*ptr;
++*ptr;
++*ptr;


while (*ptr) {

--ptr;

++*ptr;

++ptr;

--*ptr;

}


++*ptr;
++*ptr;
++*ptr;
++*ptr;

++*ptr;
++*ptr;
++*ptr;
++*ptr;

while (*ptr) {

--ptr;

++*ptr;
++*ptr;
++*ptr;

++*ptr;
++*ptr;
++*ptr;

++ptr;

--*ptr;

}

--ptr;

putchar(*ptr);

return 0;}
