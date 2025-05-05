#include <cuda_runtime.h>

__device__ int fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

__global__ void fibonacci_cuda(int* d_result, int N) {
    int idx = threadIdx.x + blockDim.x * blockIdx.x;
    if (idx < N) {
        d_result[idx] = fibonacci(idx);
    }
}
