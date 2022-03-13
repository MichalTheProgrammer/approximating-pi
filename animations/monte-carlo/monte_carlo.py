import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import random
import time

FRAMES=100
FREEZE_FRAMES=100
BATCH_SIZE=100

fig, ax = plt.subplots()
matC, = ax.plot([], [], 'ro', ms=4)
matS, = ax.plot([], [], 'bo', ms=4)
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
draw_circle = plt.Circle((0.5, 0.5), 0.5, fill=False)
draw_square = plt.Rectangle((0, 0), 1, 1, fill=False)
ax.set_aspect(1)
ax.add_artist(draw_circle)
ax.add_artist(draw_square)
ax.set_title(f'$\pi$ = 0',loc='center'),

xc = []
yc = []
xs = []
ys = []

def init():
    matC.set_data([],[])
    matS.set_data([],[])
    return matC, matS

def update(i):
    if i%10 == 0:
        print(i)
    if i >= FRAMES:
        return matC, matS
    for batch in range(BATCH_SIZE):
        x = random.random()
        y = random.random()
        if (x-0.5)**2+(y-0.5)**2 <= 0.25:
            global xc
            xc += [x]
            global yc
            yc += [y]
        else:
            global xs
            xs += [x]
            global ys
            ys += [y]
    matC.set_data(xc, yc)
    matS.set_data(xs, ys)

    areaC=len(xc)
    areaS=(len(xc)+len(xs))
    pi = areaC/areaS*4
    ax.set_title(f'$\pi$ = {pi}'),
    return matC, matS

anim = FuncAnimation(fig, update, interval=5, frames=FRAMES+FREEZE_FRAMES, init_func=init, blit=True, repeat=False)
anim.save('monte_carlo.gif', fps=25)
