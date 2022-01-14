int main(void){
 int *c = NULL;
 int a = 3, b = 4;
 printf("%d\n", a); // Ausgabe 1
 c = &b;
 *c = 5;
 printf("%d\n", b); // Ausgabe 2
 printf("%d\n", *c); // Ausgabe 3
 b = *c;
 *c = b+100;
 printf("%p\n" , c); // Ausgabe 4
 printf("%d\n" , *c); // Ausgabe 5
 printf("%p\n" , &c); // Ausgabe 6
 printf("%d\n" , b); // Ausgabe 7
 printf("%p\n" , &b); // Ausgabe 8
 printf("%d\n", a); // Ausgabe 9
}