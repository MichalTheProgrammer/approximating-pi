import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

FRAMES=30
FREEZE_FRAMES=50

fig,ax=plt.subplots()
title,=ax.text(1.25,0,''),
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_aspect(1)

circle=plt.Circle((0, 0), 1, fill=0)
roots=[]
x=[]
y=[]
polygon,=ax.plot([], [], 'b', ms=4)
ax.add_artist(polygon)

def init():
    polygon.set_data([],[])
    title.set_text("n = 0")
    return polygon, title,
def update(n):
    if (n > FRAMES) or (n < 3):
        return polygon, title,
    global x
    x=[]
    global y
    y=[]
    for k in range(0,n):
        root = np.exp(2*np.pi*1j*k/n)
        x.append(root.real)
        y.append(root.imag)
    x+=[x[0]]
    y+=[y[0]]
    title.set_text(f'n = {n}')
    polygon.set_data(x, y)
    ax.add_artist(circle)
    # plt.show()
    return polygon, title,
anim = FuncAnimation(fig, update, interval=300, frames=FRAMES+FREEZE_FRAMES, init_func=init, blit=True, repeat=False)
anim.save('polygons.gif', dpi=400)
