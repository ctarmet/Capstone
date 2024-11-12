import numpy as np
from random import random, randint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

'''
4: Tetrahedron
6: Octahedron
8: Cube
12: Icosahedron
20: Dodecahedron
'''

def poly(n):
    if n == 4:
        # Finding the vertices of a tetrahedron
        vertices = np.array([[1,0,-1/(2**0.5)], [-1,0,-1/(2**0.5)],
                             [0,1,1/(2**0.5)],[0,-1,1/(2**0.5)]])
    
    if n == 6:
        # Finding the vertices of an octahedron
        vertices = np.array([[0,0,0], [1,0,0], [0,1,0], 
                             [1,1,0],[0.5,0.5,1/(2**0.5)],
                             [0.5,0.5,-1/(2**0.5)]]) 

    if n == 8:
        # Finding the vertices of a cube
        vertices = np.array([[0,0,0], [1,0,0], [0,1,0], [0,0,1], 
                             [1,1,0], [1,0,1], [0,1,1], [1,1,1]])

    if n == 12:
        # Finding the vertices of an icosahedron
        phi = (1+math.sqrt(5))/2
        a = 1
        b = phi
        vertices = np.array([[-a, -b, 0], [a, -b, 0], [-a, b, 0], 
                             [a, b, 0], [0, -a, -b], [0, a, -b], 
                             [0, -a, b], [0, a, b], [-b, 0, -a], 
                             [-b, 0, a], [b, 0, -a], [b, 0, a] ])

    if n == 20:
        # Finding the vertices of a dodecahedron
        phi = (1+math.sqrt(5))/2
        a = 1
        b = phi
        c = a+b

        vertices = np.array([[-b,-b,-b], [b,-b,-b], [-b,b,-b], [b,b,-b], 
                             [-b,-b,b], [b,-b,b], [-b,b,b], [b,b,b], 
                             [c, -a, 0], [c, a, 0], [-c, -a, 0], [-c, a, 0],
                             [a, 0, -c], [-a, 0, -c], [a, 0, c], [-a, 0, c], 
                             [0, -c, -a], [0, -c, a], [0, c, -a], [0, c, a]])
    return vertices


def randpt():
    # Three random numbers between 0 and 1 will create the coordinates for the initial point
    x = random()
    y = random()
    z = random()

    return (x, y, z)

def chaos(n, frac, i):
    # Finding the vertices of the polyhedron
    vertices = poly(n)

    # Initiating the current point
    current_point = randpt()
    xs = []
    ys = []
    zs = []
    colors = []

    # Create a colormap
    colormap = plt.cm.rainbow

    # Finding the i points
    for _ in range(i):
        # Selecting the random vertex and finding the vector to it
        random_index = randint(0, n - 1)
        random_vertex = vertices[random_index]
        vector_to_vertex = np.array(random_vertex) - np.array(current_point)

        # Finding the new point
        new_point = np.array(current_point) + vector_to_vertex * frac
        if _ > 5:
            xs.append(new_point[0])
            ys.append(new_point[1])
            zs.append(new_point[2])
            # Assign color based on the selected vertex using the rainbow colormap
            colors.append(colormap(random_index / (n - 1)))  # Normalize index for colormap
       
        current_point = new_point
    
    # 3D plot using Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(xs, ys, zs, c=colors, s=0.5)

    # Display the plot
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Run the Chaos Game with the tetrahedron (4 vertices) and 100,000 iterations
chaos(4, 0.5, 100000)
# You can uncomment and run with other polyhedra
# chaos(6, 0.5, 100000)
# chaos(8, 0.5, 100000)
# chaos(12, 0.618, 100000) # Optimal 1/phi = 0.618...
# chaos(20, 0.7236, 100000) # dodecahedron with optimal ratio
