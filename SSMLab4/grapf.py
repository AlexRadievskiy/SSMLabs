import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

timestamp = (1.2, 2.1, 3.1, 3.9, 4.8)

distance = (3.4142, 2.9818, 3.3095, 3.8184, 4.3599)

plt.plot(timestamp, distance, 'o')

plt.show()

data = np.array((timestamp, distance))

tck, u = interpolate.splprep(data, s=0)

unew = np.arange(0, 1.01, 0.01)

out = interpolate.splev(unew, tck)

plt.plot(out[0], out[1], color='orange')

plt.plot(data[0, :], data[1, :], 'ob')

plt.show()
