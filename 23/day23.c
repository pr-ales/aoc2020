#include <stdio.h> 
#include <stdlib.h>

int check3(long **ptrs_next, long *ptr, int val) {
    for (int i = 0; i < 3; i++) {
        long val_ptr = *ptr;
        if (val_ptr == val) {
            return 1;
        }
        ptr = ptrs_next[val_ptr];
    }

    return 0;
}

void shuffle(long count, long *input, long padding, long n_iter) {
    long size = count > padding ? count : padding;
    
    
    long *cups = calloc(size, sizeof(long));
    long **ptrs_next = calloc(size, sizeof(long*));
    
    // now it does not segfault, but maybe it leaks... C is hard
    for (long i = 0; i < size; i++) {
        ptrs_next[i] = malloc(sizeof(long*));
    }
    
    for (long i = 0; i < size; i++) {
        cups[i] = i < count ? input[i] : i + 1;
        ptrs_next[cups[i]] = &cups[(i + 1) % size];
    }
    
    long current = cups[0];
    
    for (long it = 0; it < n_iter; it++) {
        
        long next = current > 1 ? current - 1 : size;
        while (check3(ptrs_next, ptrs_next[current], next)) {
            next = next > 1 ? next - 1 : size;
        }
        
        long *seam = ptrs_next[current];
        long cut = *ptrs_next[current];
        for (long i = 0; i < 3; i++) {
            cut = *ptrs_next[current];
            ptrs_next[current] = ptrs_next[*ptrs_next[current]];
            
        }
        
        ptrs_next[cut] = ptrs_next[next];
        ptrs_next[next] = seam;
        
        current = *ptrs_next[current];
        
//         if (size < 10) {
//             long *ptr = ptrs_next[1];
//             for (long i = 0; i < size - 1; i++) {
//                 printf("%ld", *ptr);
//                 ptr = ptrs_next[*ptr];
//             }
//             printf("\n");
//         }
    }
    
    long *ptr = ptrs_next[1];
    if (size < 10) {
        for (long i = 0; i < size - 1; i++) {
            printf("%ld", *ptr);
            ptr = ptrs_next[*ptr];
        }
        printf("\n");
    } else {
        long result = 1;
        for (long i = 0; i < 2; i++) {
            printf("%ld: %ld\n", i + 1, *ptr);
            result *= *ptr;
            ptr = ptrs_next[*ptr];
        }
        printf("%ld\n", result);
    }
    
    free(cups);
  
    free(ptrs_next);
}

int main() {
    long input[] = {2, 5, 3, 1, 4, 9, 8, 6, 7};
    //long input[] = {3, 8, 9, 1, 2, 5, 4, 6, 7};
    
    shuffle(9, input, 0, 100);
    shuffle(9, input, 1000000, 10000000);
    
    return 0;
}
