
# coding: utf-8

# In[167]:


import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
import matplotlib.patches as patches

plt.style.use('ggplot')

checkpoint_sigma = 0.1
sigma = 0.2 
sqare_size = 0.4
i = 4

fig = plt.figure()
fig.set_size_inches(12, 8, True)
ax = plt.axes(aspect='equal', autoscale_on=True)
ax.set_xlim(0.0, 8.0), ax.set_xticks([])
ax.set_ylim(0.0, 8.0), ax.set_yticks([])
checkpoints = [];

def init():
     # horizontals 
    plt.plot([0.5, 7.0], [1.5, 1.5], 'k')
    plt.plot([0.5, 7.0], [3.0, 3.0], 'k')
    plt.plot([0.5, 7.0], [4.5, 4.5], 'k')
    plt.plot([0.5, 7.0], [6.0, 6.0], 'k')
    # verticals 
    plt.plot([1.5, 1.5], [0.5, 7.0], 'k')
    plt.plot([3.0, 3.0], [0.5, 7.0], 'k')
    plt.plot([4.5, 4.5], [0.5, 7.0], 'k')
    plt.plot([6.0, 6.0], [0.5, 7.0], 'k')
    # trafficlights
    for k in range(0,i):
        for j in range(0,i):
            ax.add_patch(patches.Rectangle((1.3 + k*1.5, 1.3 + j*1.5),  sqare_size, sqare_size))
    for k in range(0,i):
        for j in range(0,i-1):
            ax.add_patch(plt.Circle((2.0 + j*1.5, 1.5 + k*1.5), radius=checkpoint_sigma, fc='r'))
            ax.add_patch(plt.Circle((2.5 + j*1.5, 1.5 + k*1.5), radius=checkpoint_sigma, fc='r'))
            ax.add_patch(plt.Circle((1.5 + k*1.5, 2.0 + j*1.5), radius=checkpoint_sigma, fc='g'))
            ax.add_patch(plt.Circle((1.5 + k*1.5, 2.5 + j*1.5), radius=checkpoint_sigma, fc='g'))
    patch.center = s_map[site[0]]
    ax.set_title('t = 0')
    return patch


def animate(i):
    ax.set_title('t = ' + str(i))
    return patch


anim = animation.FuncAnimation(fig, animate,init_func=init,frames=N_runs,interval=1000,repeat=False)

from IPython.display import HTML
HTML(anim.to_jshtml())

