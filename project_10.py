import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure()

a, b, c = 3, 3, 16

x_coord = np.linspace(-5, 5, 100)
y_coord = np.zeros(100)

for i in range(0, 100, 1):
    y_coord[i] = a * x_coord[i]**2 + b * x_coord[i] + c

prb = plt.plot(x_coord, y_coord, color='r')
anim_list = []

for i in range(0, 100, 1):
    anim_odj, = plt.plot(x_coord[i], y_coord[i], 'bo', ms=10)
    anim_list.append([anim_odj])
plt.axis('equal')
ani = ArtistAnimation(fig, anim_list, interval=50)
ani.save('ani_1a.html')