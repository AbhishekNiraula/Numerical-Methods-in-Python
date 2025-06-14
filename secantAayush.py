import matplotlib.pyplot as plt
import numpy as np
import math

# Define the function
def f(x):
    return (x**3 + 2 - x)**0.5
# Truncation to 3 decimal places (not rounding)
def truncate_to_3_decimal(x):
    return int(x * 1000) / 1000

# Secant Method implementation
def secant_method(x0, x1, max_iter=100):
    print("Secant Method (Stopping when root correct to 3 decimal places)")
    print(f"{'Iter':<5} {'x0':<12} {'x1':<12} {'x_new':<12} {'f(x_new)':<15}")
    print("-" * 60)

    prev_trunc_x = None
    iteration = 1

    while iteration <= max_iter:
        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            print("Zero division error in secant formula.")
            break

        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fx_new = f(x_new)
        trunc_x = truncate_to_3_decimal(x_new)

        print(f"{iteration:<5} {x0:<12.6f} {x1:<12.6f} {x_new:<12.6f} {fx_new:<15.10f}")

        if prev_trunc_x is not None and trunc_x == prev_trunc_x:
            print(f"\n✅ Final Root (correct to 3 decimal places): {trunc_x:.3f}")
            print(f"🔁 Total Iterations: {iteration}")
            return trunc_x

        x0, x1 = x1, x_new
        prev_trunc_x = trunc_x
        iteration += 1

    print("\n⚠️ Method did not converge.")
    return None

# Run secant method on two initial points
root = secant_method(1,2)