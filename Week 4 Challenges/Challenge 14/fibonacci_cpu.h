#include <iostream>
#include <vector>
#include <chrono>

void fibonacci_cpu(int* result, int N) {
    if (N > 0) result[0] = 0;
    if (N > 1) result[1] = 1;
    for (int i = 2; i < N; i++) {
        result[i] = result[i - 1] + result[i - 2];
    }
}
