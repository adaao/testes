#include <stdio.h>

int main() {
    int one_bilion = 1000000000;
    int index;
    int counting = 0;

    for(index = 0; index < one_bilion; index++){
        counting = counting + 1;
    }

    printf("%i", counting);
}