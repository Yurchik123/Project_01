import numpy as np
import pygame
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
#
# pygame.mixer.pre_init(44100, -16, 2, 2048)
# pygame.init()
# screen = pygame.display.set_mode((1000, 1000))
# pygame.display.set_caption("Project_03")
t = np.arange(0, 200 * 24 * 60 * 60, 3600)


def diff_func(s, t):
    x1, v_x1, y1, v_y1, x2, v_x2, y2, v_y2 = s

    dx1dt = v_x1
    dv_x1dt = - G * M2 / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (3 / 2) * (x1 - x2)

    dy1dt = v_y1
    dv_y1dt = - G * M2 / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (3 / 2) * (y1 - y2)

    dx2dt = v_x2
    dv_x2dt = - G * M1 / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (3 / 2) * (x2 - x1)

    dy2dt = v_y2
    dv_y2dt = - G * M1 / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (3 / 2) * (y2 - y1)

    return dx1dt, dv_x1dt, dy1dt, dv_y1dt, dx2dt, dv_x2dt, dy2dt, dv_y2dt


G = 6.7 * 10 ** (-11)
M1 = 600000000
M2 = 1000

x10 = 0
y10 = 0

x20 = 0
y20 = 100

v_1x0 = 100
v_1y0 = 0

v_2x0 = 1
v_2y0 = 0

s0 = x10, v_1x0, y10, v_1y0, x20, v_2x0, y20, v_2y0

sol = odeint(diff_func, s0, t)

plt.plot(sol[:, 0], sol[:, 2], 'g-', label='Sun')
plt.plot(sol[:, 4], sol[:, 6], 'b-', label='Earth')
plt.legend()
plt.show()

# anim_list = []
# fig = plt.figure()
#
# for i in range(0, len(t), 1):
#     sun, = plt.plot(sol[i, 1], sol[i, 3], 'go', label='Sun', ms=10)
#     earth, = plt.plot(sol[i, 5], sol[i, 7], 'bo', label='Earth')
#     anim_list.append([sun, earth])
#
# plt.axis('equal')
# ani = ArtistAnimation(fig, anim_list, interval=50)
# ani.save('ani.html')

# while running:
#     pygame.time.delay(1)
#     pygame.display.flip()
#     screen.fill((255, 255, 255))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 pygame.quit()
#                 quit()
#
#     pygame.draw.circle(screen, (180, 0, 0), )