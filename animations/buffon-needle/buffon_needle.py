import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.collections import LineCollection
import random

FRAMES=100
FREEZE_FRAMES=100
BATCH_SIZE=100

fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.grid(axis='x')
ax.set_aspect(1)
ax.set_title(f'$\pi$ = 0',loc='center'),

linesX = (0, 0.2, 0.4, 0.6, 0.8, 1)
def crossLine(x1,x2):
    if x1 > x2:
        x1,x2=x2,x1
    for lx in linesX:
        if x1 <= lx <= x2:
            return True
    return False

R=0
N=0
def update(i):
    if i%10 == 0:
        print(i)
    if i >= FRAMES:
        return
    linesR=[]
    linesB=[]
    for batch in range(BATCH_SIZE):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        a = random.uniform(0, 360)
        sin = np.sin(np.radians(a))
        cos = np.cos(np.radians(a))
        line = [(x+0.05*sin, y+0.05*cos), (x-0.05*sin, y-0.05*cos)]
        if crossLine(line[0][0], line[1][0]):
            linesR += [line]
            global R
            R+=1
        else:
            linesB += [line]
        global N
        N+=1
    pi = 2*0.1*N/(0.2*R)
    ax.set_title(f'$\pi$ = {pi}')
    ax.add_collection(LineCollection(linesR, colors=['r' for x in range(len(linesR))]))
    ax.add_collection(LineCollection(linesB, colors=['b' for x in range(len(linesB))]))

ani = FuncAnimation(fig=fig, func=update, interval=1, frames=FRAMES+FREEZE_FRAMES)
ani.save('needle.gif', fps=25)
