import subprocess
import time

def benchmark(script_path, label, runs=5):
    total = 0
    print(f"Benchmarking {label} version...")
    for i in range(runs):
        start = time.time()
        subprocess.run(["python3", script_path], capture_output=True)
        end = time.time()
        elapsed = end - start
        total += elapsed
        print(f"  Run {i+1}: {elapsed:.4f} seconds")
    avg = total / runs
    print(f"Average time for {label}: {avg:.4f} seconds\n")
    return avg

cpu_time = benchmark("frozenlake_cpu.py", "CPU")
gpu_time = benchmark("frozenlake_gpu.py", "GPU")

speedup = cpu_time / gpu_time if gpu_time > 0 else float('inf')
print(f"Speed-up (CPU/GPU): {speedup:.2f}x")
