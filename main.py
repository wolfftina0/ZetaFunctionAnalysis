
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a simple plot
plt.plot(x, y)
plt.title('Simple Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)

# Save the plot (since we can't display it directly in console)
plt.savefig('sine_wave.png')
