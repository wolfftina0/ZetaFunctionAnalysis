
from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np
from mpmath import zetazero, zeta
import io

app = Flask(__name__)

def modified_zeta_zeros(include_zero=False, num_zeros=10):
    zeros = [complex(zetazero(n)) for n in range(1, num_zeros + 1)]
    if include_zero:
        zeros = [0] + zeros
    return [float(z.imag) for z in zeros]  # Extract imaginary parts

@app.route('/')
def plot():
    plt.figure(figsize=(12, 6))
    
    # Parameters
    num_zeros = 50
    
    # Compute zeros
    zeros_with_zero = modified_zeta_zeros(include_zero=True, num_zeros=num_zeros)
    zeros_without_zero = modified_zeta_zeros(include_zero=False, num_zeros=num_zeros)
    
    # Create plots
    plt.plot(range(1, len(zeros_without_zero) + 1), zeros_without_zero, 
             label="Without 0 as prime", marker="o")
    plt.plot(range(1, len(zeros_with_zero) + 1), zeros_with_zero, 
             label="With 0 as prime", marker="x")
    
    plt.xlabel("Zero Index")
    plt.ylabel("Imaginary Part of Zeros")
    plt.title("Distribution of Non-Trivial Zeros of Zeta Function")
    plt.legend()
    plt.grid(True)
    
    # Save plot to memory buffer
    img = io.BytesIO()
    plt.savefig(img)
    img.seek(0)
    plt.close()
    
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
