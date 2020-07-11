import numpy as np
from matplotlib import pyplot as plt

hx = hy = 0.25
size = max(hx, hy)

lower_x, upper_x = -5, 5
lower_y, upper_y = -5, 5

# dy / dx = f(x,y)
def f(x, y):
    return 1-x*y



def plot_direction_field():
    x_coords_range = [np.arange(lower_x, upper_x+hx, hx)]
    y_coords_range = [np.arange(lower_y, upper_y+hy, hy)]
    coordinates = np.array(np.meshgrid(x_coords_range, y_coords_range)).T.reshape(-1, 2)

    for coord in coordinates:
        slope = f(coord[0], coord[1])

        # Plot arrow
        angle = np.arctan(slope)
        x1 = coord[0]
        y1 = coord[1]
        dx = size * np.cos(angle)
        dy = size * np.sin(angle)

        plt.arrow(x1, y1, dx, dy, shape='full', color='#008800', length_includes_head=True,
                 zorder=0, head_length=size/2, head_width=size/4)

    plt.scatter(coordinates[:,0], coordinates[:,1], s=size, color='#8601AF')

def draw_IVP(x0, y0, color='#000000'):
    x = []
    y = []
    
    prev_x, prev_y = x0, y0
    while lower_x <= prev_x <= upper_x and lower_y <= prev_y <= upper_y:
        # Find the angle of the slope
        angle = np.arctan(f(prev_x, prev_y))

        # Separate slope into its components
        dx = size * np.cos(angle)
        dy = size * np.sin(angle)

        prev_x -= dx
        prev_y -= dy

        x.insert(0, prev_x)
        y.insert(0, prev_y)


    next_x, next_y = x0, y0
    while lower_x <= next_x <= upper_x and lower_y <= next_y <= upper_y:
        # Find the angle of the slope
        angle = np.arctan(f(next_x, next_y))

        # Separate slope into its components
        dx = size * np.cos(angle)
        dy = size * np.sin(angle)

        next_x += dx
        next_y += dy

        x.append(next_x)
        y.append(next_y)


    plt.plot(x, y, color=color)



plot_direction_field()
draw_IVP(0, 0, color='#FE2712')
draw_IVP(-1, 0, color='#FB9902')
draw_IVP(2, 2, color='#FEFE33')
draw_IVP(0, -4, color='#0247FE')


plt.show()
