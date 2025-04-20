# parallel_diff_eq_solver.py
from multiprocessing import Pool

def euler_step(args):
    t, y, step_size = args
    return (t, y)

def solve_diff_eq_parallel(y0, t0, t_end, step_size):
    t_values = [t0 + i * step_size for i in range(int((t_end - t0) / step_size) + 1)]
    y = y0
    values = []
    for t in t_values:
        values.append((t, y))
        y = y - 2 * y * step_size
    return values

if __name__ == "__main__":
    result = solve_diff_eq_parallel(1.0, 0.0, 5.0, 0.1)
    for t, y in result:
        print(f"t={t:.1f}, y={y:.4f}")
