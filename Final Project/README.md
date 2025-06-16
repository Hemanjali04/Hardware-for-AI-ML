# Hardware-Accelerated CNN for Fashion MNIST Image Classification

**Author**: Hemanjali Geridipudi  
**Institution**: Portland State University  
**Email**: geridi@pdx.edu  
**Date**: June 2025  

## Abstract

This project presents a complete pipeline for hardware-accelerated inference of a Convolutional Neural Network (CNN) trained on the Fashion MNIST dataset. The CNN model was developed and trained using Keras, achieving ~93% accuracy. To improve performance and reduce latency, core bottlenecks like Conv2D, ReLU, MaxPooling, and SoftMax were implemented in hardware using Vitis HLS 2025.1, targeting an Artix-7 FPGA. Fixed-point arithmetic (`ap_fixed<16,6>`) and optimization directives like loop pipelining were used to achieve parallelism. The modules were synthesized into Verilog, tested for correctness, and yielded significant speedup over the software model.

## 1. Introduction

CNNs are widely used in image classification but are computationally heavy due to large numbers of MAC operations. FPGA acceleration offers a path to real-time inference by enabling pipelined and parallel processing. This project targets CNN acceleration for Fashion MNIST using HLS-based design on an Artix-7 FPGA.

## 2. Background

The CNN architecture includes:
- **Conv + ReLU**
- **MaxPooling**
- **Fully Connected + SoftMax**

Each block increases in channel width and is optimized for inference. Figure 1 in the full report illustrates the architecture.

## 3. Bottlenecks

- **Conv2D**: Dominant compute workload, ideal for MAC parallelism on FPGA.
- **Floating-point arithmetic**: Replaced with fixed-point for speed and hardware efficiency.

## 4. Methodology

1. Trained a CNN using Keras (~93% test accuracy).
2. Identified Conv2D, MaxPooling, and SoftMax as bottlenecks.
3. Implemented these layers in HLS using fixed-point and pipeline directives.
4. Combined MaxPooling + SoftMax in one HLS module.
5. Verified accuracy with testbenches comparing against software outputs.

**Tools**: Vitis HLS 2025.1, Vivado, Artix-7 FPGA

## 5. Results

### Software Accuracy
- ~93% test accuracy
- 99% training accuracy after 50 epochs

### Performance Metrics

| Component         | Software Latency | HLS Latency   | Speedup |
|------------------|------------------|---------------|---------|
| Conv2D + ReLU    | ~0.05 ms         | ~0.003 ms     | ~16×    |
| MaxPooling       | ~0.001 ms        | ~0.00003 ms   | ~33×    |
| SoftMax          | ~0.02 ms         | ~0.0005 ms    | ~40×    |
| **Total**        | ~0.23 ms         | ~0.01 ms      | ~23×    |

### Throughput

| Platform         | Images/Second |
|------------------|----------------|
| CPU (Software)   | ~4,300 FPS     |
| FPGA (Hardware)  | ~40,000 FPS    |

## 6. Conclusion

This project achieved a 20× speedup using HLS-based acceleration on an Artix-7 FPGA with minimal loss in accuracy. The implementation demonstrates feasibility for real-time edge AI inference using FPGAs.

## 📚 References

1. Y. Liang et al., *Sensors*, 2024.  
2. J. Jiang et al., *arXiv:2505.13461*, May 2025.  
3. H. Yang et al., *IEEE TCAD*, 2017.  
4. T. Yan et al., *Remote Sensing*, 2022.
