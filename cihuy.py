import numpy as np
import matplotlib.pyplot as plt

f = 2
fs = 30
n = np.arange(0, 1, 1/fs)
x_discrete = np.sin(2 * np.pi * f * n)

plt.figure()
plt.stem(n, x_discrete, basefmt=" ")
plt.title('Discrete-Time Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

print("aduh ganteng nya~~")