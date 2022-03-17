int main(void){
 int *c = NULL;
 int a = 3, b = 4;
 printf("%d\n", a); // Ausgabe 1 --= 3
 c = &b;
 *c = 5;
 printf("%d\n", b); // Ausgabe 2 --= 5
 printf("%d\n", *c); // Ausgabe 3 --= 5
 b = *c;
 *c = b+100;
 printf("%p\n" , c); // Ausgabe 4 -- = Adresse von B
 printf("%d\n" , *c); // Ausgabe 5 --= 105
 printf("%p\n" , &c); // Ausgabe 6 --= Adresse von C
 printf("%d\n" , b); // Ausgabe 7 --= 105
 printf("%p\n" , &b); // Ausgabe 8 --= Adresse von B
 printf("%d\n", a); // Ausgabe 9 --= 3
}