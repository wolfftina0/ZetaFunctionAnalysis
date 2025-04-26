
from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def plot():
    # Generate plot
    plt.figure(figsize=(8, 6))
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Simple Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    
    # Save plot to memory buffer
    img = io.BytesIO()
    plt.savefig(img)
    img.seek(0)
    plt.close()
    
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
