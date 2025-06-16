#include "conv2d_relu.h"

void conv2d_relu(
    fixed_t input[IN_HEIGHT][IN_WIDTH],
    fixed_t kernel[KERNEL_SIZE][KERNEL_SIZE],
    fixed_t output[OUT_HEIGHT][OUT_WIDTH])
{
    // Partition both dimensions of the input array for full parallel access
    #pragma HLS ARRAY_PARTITION variable=input complete dim=1
    #pragma HLS ARRAY_PARTITION variable=input complete dim=2
    #pragma HLS ARRAY_PARTITION variable=kernel complete dim=1
    #pragma HLS ARRAY_PARTITION variable=kernel complete dim=2
    #pragma HLS ARRAY_PARTITION variable=output complete dim=1
    #pragma HLS ARRAY_PARTITION variable=output complete dim=2

    // Enable pipelining of the loop
    #pragma HLS PIPELINE

    for (int i = 0; i < OUT_HEIGHT; i++) {
        for (int j = 0; j < OUT_WIDTH; j++) {
            fixed_t sum = 0;

            // Unroll inner loops for kernel operation
            for (int ki = 0; ki < KERNEL_SIZE; ki++) {
                for (int kj = 0; kj < KERNEL_SIZE; kj++) {
                    #pragma HLS UNROLL
                    sum += input[i + ki][j + kj] * kernel[ki][kj];
                }
            }

            // Apply ReLU
            output[i][j] = (sum > 0) ? sum : (fixed_t)0;
        }
    }
}
