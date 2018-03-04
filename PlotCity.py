
# coding: utf-8

# In[ ]:


import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
import matplotlib.patches as patches

plt.style.use('ggplot')

class PlotCity:
    checkpoint_sigma = 0.1
    sigma = 0.2 
    sqare_size = 0.4
    i = 4
    fig = plt.figure()
    fig.set_size_inches(12, 8, True)
    ax = plt.axes(aspect='equal', autoscale_on=True)
    ax.set_xlim(0.0, 8.0), ax.set_xticks([])
    ax.set_ylim(0.0, 8.0), ax.set_yticks([])
    
    def plot_horizontal_lines():
        plt.plot([0.5, 7.0], [1.5, 1.5], 'k')
        plt.plot([0.5, 7.0], [3.0, 3.0], 'k')
        plt.plot([0.5, 7.0], [4.5, 4.5], 'k')
        plt.plot([0.5, 7.0], [6.0, 6.0], 'k')
    
    def plot_vertical_lines():
        plt.plot([1.5, 1.5], [0.5, 7.0], 'k')
        plt.plot([3.0, 3.0], [0.5, 7.0], 'k')
        plt.plot([4.5, 4.5], [0.5, 7.0], 'k')
        plt.plot([6.0, 6.0], [0.5, 7.0], 'k')
        
    def plot_trafficlights_and_capacity_points(trafficlights, state):
        for k in range(0,i):
            for j in range(0,i):
                ax.add_patch(patches.Rectangle((1.3 + k*1.5, 1.3 + j*1.5),  sqare_size, sqare_size)
                for counter in trafficlights[k][j].counters:
                    if(counter < 5):
                        ax.add_patch(plt.Circle((2.0 + col*1.5, 1.5 + row*1.5), radius=checkpoint_sigma, fc='g'))
                    elif(counter < 8):
                        ax.add_patch(plt.Circle((2.0 + col*1.5, 1.5 + row*1.5), radius=checkpoint_sigma, fc='y'))
                    else:
                        ax.add_patch(plt.Circle((2.0 + j*1.5, 1.5 + k*1.5), radius=checkpoint_sigma, fc='r'))
        
        
    def plot_city_state(city, state):
        trafficlights[][] = city.get_traffic_lights                   
        plot_horizontal_lines()
        plot_vertical_lines()
        plot_trafficlights_and_capacity_points(trafficlights, state)
        patch.center = s_map[site[0]]                            
        ax.set_title('t = ' + state)
        return patch

