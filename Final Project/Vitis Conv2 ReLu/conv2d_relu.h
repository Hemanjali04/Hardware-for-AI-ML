
#ifndef CONV2D_RELU_H
#define CONV2D_RELU_H

#include <ap_fixed.h>

#define IN_WIDTH 28
#define IN_HEIGHT 28
#define KERNEL_SIZE 3
#define OUT_WIDTH (IN_WIDTH - KERNEL_SIZE + 1)
#define OUT_HEIGHT (IN_HEIGHT - KERNEL_SIZE + 1)

typedef ap_fixed<16,6> fixed_t;

void conv2d_relu(
    fixed_t input[IN_HEIGHT][IN_WIDTH],
    fixed_t kernel[KERNEL_SIZE][KERNEL_SIZE],
    fixed_t output[OUT_HEIGHT][OUT_WIDTH]
);

#endif
