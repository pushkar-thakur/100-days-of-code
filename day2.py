import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Sine Wave', color='blue', linewidth=2)
plt.title('Simple Sine Wave Plot')
plt.xlabel('x values (radians)')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
