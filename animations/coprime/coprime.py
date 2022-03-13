import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

FRAMES=250
FREEZE_FRAMES=100
BATCH_SIZE=1

MAX_NUM=int(1e9)

fig, ax = plt.subplots()
ax.set_title('Pi = 0',loc='center'),
plt.xlabel('Number of iterations')
plt.axhline(y=np.pi, color='r', linestyle='-')

coprime=0
n=0
dataX=[]
dataY=[]

def update(i):
    if i%10 == 0:
        print(i)
    if i >= FRAMES:
        return
    a = random.randint(1, MAX_NUM)
    b = random.randint(1, MAX_NUM)
    for batch in range(BATCH_SIZE):
        if np.gcd(a,b) == 1:
            global coprime
            coprime+=1
        global n
        n+=1
        pi = 0 if coprime==0 else (6/(coprime/n))**0.5
        global dataX, dataY
        dataX+=[i]
        dataY+=[pi]
    ax.plot(dataX, dataY, scaley=True, scalex=True, color="b", ms=1)
    ax.set_title(f'Pi = {pi}')

anim = FuncAnimation(fig=fig, func=update, interval=1, frames=FRAMES+FREEZE_FRAMES)
anim.save('coprime.gif', fps=25)
