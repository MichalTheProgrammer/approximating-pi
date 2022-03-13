import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

FRAMES=150
FREEZE_FRAMES=100
n=10000
r=1
fx=[]
for i in range(3, n):
    l = r * 2 * math.sin(math.radians(360 / 2 / i))
    fx += [(l * i)/(2 * r)]
x1=range(len(fx))
x,y=[],[]

fig, ax = plt.subplots()
ax.set_title('$\pi$ = 0',loc='center'),
plt.xlabel('Number of polygon\'s sides')
plt.axhline(y=math.pi, color='r', linestyle='-')

def update(i):
    if i >= 3 and i < FRAMES:
        x.append(x1[i])
        y.append(fx[i])
        ax.plot(x, y, scaley=True, scalex=True, color="b", ms=1)
        ax.set_title(f'$\pi$ = {fx[i]}')

anim = FuncAnimation(fig=fig, func=update, frames=FRAMES+FREEZE_FRAMES, repeat=False)
anim.save('demo.gif', fps=20, dpi=400)
