# diff_eq_solver.py
def solve_diff_eq(y0, t0, t_end, step_size):
    t = t0
    y = y0
    result = []
    while t <= t_end:
        result.append((t, y))
        y = y - 2 * y * step_size  # dy/dt = -2y
        t += step_size
    return result

if __name__ == "__main__":
    solution = solve_diff_eq(1.0, 0.0, 5.0, 0.1)
    for t, y in solution:
        print(f"t={t:.1f}, y={y:.4f}")
