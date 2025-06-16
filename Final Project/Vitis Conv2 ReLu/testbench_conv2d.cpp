
#include <iostream>
#include <fstream>
#include "conv2d_relu.h"

int main() {
    fixed_t input[IN_HEIGHT][IN_WIDTH];
    fixed_t kernel[KERNEL_SIZE][KERNEL_SIZE];
    fixed_t output[OUT_HEIGHT][OUT_WIDTH];

    // Initialize input with sample values
    for (int i = 0; i < IN_HEIGHT; i++) {
        for (int j = 0; j < IN_WIDTH; j++) {
            input[i][j] = (i + j) % 8;
        }
    }

    // Define a simple edge detection kernel
    fixed_t kernel_vals[3][3] = {{1, 0, -1}, {1, 0, -1}, {1, 0, -1}};
    for (int i = 0; i < KERNEL_SIZE; i++) {
        for (int j = 0; j < KERNEL_SIZE; j++) {
            kernel[i][j] = kernel_vals[i][j];
        }
    }

    // Run convolution with ReLU
    conv2d_relu(input, kernel, output);

    // Print to terminal
    for (int i = 0; i < OUT_HEIGHT; i++) {
        for (int j = 0; j < OUT_WIDTH; j++) {
            std::cout << output[i][j].to_float() << " ";
        }
        std::cout << std::endl;
    }

    // Save output to a fixed location on Desktop
    std::ofstream fout("C:/Users/gerid/Desktop/VitisCNNWorkspace/output_result.txt");
    for (int i = 0; i < OUT_HEIGHT; i++) {
        for (int j = 0; j < OUT_WIDTH; j++) {
            fout << output[i][j].to_float() << " ";
        }
        fout << std::endl;
    }
    fout.close();

    return 0;
}
