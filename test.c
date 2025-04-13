#include <stdio.h>
#include "custom.h"

int main() {
    char c = 'A';
    int x = 042;
    int h = 0x1F4;
    float y = 3.14;
    const char* msg = "Hola\n";

    if (x > 0 && y <= 10.0) {
        printf("%s", msg);
    }

    x = x + 1;
    y = y * 2.0;

    return 0;
}

// Esto es un comentario
/* Este también lo es */

int error = 10 @ 5;
