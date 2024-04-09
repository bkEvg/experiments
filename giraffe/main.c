//
//  main.c
//  giraffe
//
//  Created by Кирилл Бауэр on 10.04.2024.
//

#include <stdio.h>
int multi(int x, int y);

int main(int argc, const char * argv[]) {
    // insert code here...
    printf("Hello, World!\n%d", multi(43, 5));
    return 0;
}

int multi(int x, int y) {
    return x * y;
}
