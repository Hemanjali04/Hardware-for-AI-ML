#include <iostream>
#include <chrono>
#include <cuda_runtime.h>

void fibonacci_cpu(int* result, int N);
__global__ void fibonacci_cuda(int* d_result, int N);

int main() {
    const int N = 220;

    // CPU
    int* cpu_result = new int[N];
    auto start_cpu = std::chrono::high_resolution_clock::now();
    fibonacci_cpu(cpu_result, N);
    auto end_cpu = std::chrono::high_resolution_clock::now();

    // GPU
    int* h_result = new int[N];
    int* d_result;
    cudaMalloc(&d_result, N * sizeof(int));

    auto start_gpu = std::chrono::high_resolution_clock::now();
    fibonacci_cuda<<<(N + 255) / 256, 256>>>(d_result, N);
    cudaDeviceSynchronize();
    cudaMemcpy(h_result, d_result, N * sizeof(int), cudaMemcpyDeviceToHost);
    auto end_gpu = std::chrono::high_resolution_clock::now();

    // Verify
    bool match = true;
    for (int i = 0; i < N; i++) {
        if (cpu_result[i] != h_result[i]) {
            match = false;
            std::cout << "Mismatch at " << i << ": CPU = " << cpu_result[i] << ", GPU = " << h_result[i] << "\n";
            break;
        }
    }

    std::chrono::duration<double> cpu_time = end_cpu - start_cpu;
    std::chrono::duration<double> gpu_time = end_gpu - start_gpu;

    std::cout << "CPU Time: " << cpu_time.count() << "s\n";
    std::cout << "GPU Time: " << gpu_time.count() << "s\n";
    std::cout << "Results match: " << (match ? "YES" : "NO") << "\n";

    cudaFree(d_result);
    delete[] cpu_result;
    delete[] h_result;

    return 0;
}
