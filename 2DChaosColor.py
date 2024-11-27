import numpy as np
from random import random, randint
import matplotlib.pyplot as plt
from matplotlib import cm  

def poly(n):
    # Find the vertices of an n-gon
    if n == 3:
        vertices = np.array([[0, 0], [1, np.sqrt(3)], [2, 0]])
    elif n == 4:
        vertices = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    elif n == 5:
        c1 = 0.25 * (np.sqrt(5) - 1)
        c2 = 0.25 * (np.sqrt(5) + 1)
        s1 = 0.25 * (np.sqrt(10 + 2 * np.sqrt(5)))
        s2 = 0.25 * (np.sqrt(10 - 2 * np.sqrt(5)))
        vertices = np.array([[-s2, -c2], [s2, -c2], [s1, c1], [0, 1], [-s1, c1]])
    elif n == 6:
        a = 0.5
        b = 0.5 * np.sqrt(3)
        vertices = np.array([[-a, -b], [a, -b], [1, 0], [a, b], [-a, b], [-1, 0]])
    elif n == 8:
        a = 1 + np.sqrt(2)
        vertices = np.array([[-1, -a], [1, -a], [-1, a], [1, a], [-a, -1], [a, -1], [-a, 1], [a, 1]])
        
    return vertices

def randpt():
    # Random initial point (x, y) between 0 and 1
    return np.array([random(), random()])  # Return as NumPy array for consistency

def chaos(n, frac, i):
    plt.figure(figsize=(6, 6))

    # Finding the vertices of the n-gon
    vertices = poly(n)

    # Initiating the current point
    current_point = randpt()

    # Use the updated colormap access method
    colormap = cm.get_cmap('rainbow', n)  # You can choose any colormap

    # Lists to store points and their corresponding colors
    x_points = []
    y_points = []
    colors = []

    # Finding the i points
    for _ in range(i):
        # Selecting the random vertex and finding the vector to it
        random_index = randint(0, n - 1)
        random_vertex = vertices[random_index]  # Already a NumPy array

        # Finding the new point
        new_point = current_point + (random_vertex - current_point) * frac

        # Accumulating the points and corresponding colors
        if _ > 5:
            x_points.append(new_point[0])
            y_points.append(new_point[1])
            colors.append(colormap(random_index))  # Use colormap for color

        # Update current point to the new point
        current_point = new_point

    # Plot all points at once with corresponding colors
    plt.scatter(x_points, y_points, c=colors, s=0.1)

    # Setting axis properties for clean plotting
    plt.axis('equal')
    plt.axis('off')
    plt.show()
    

# Running the Chaos Game for an n-gon (e.g., triangle) with 100,000 iterations
chaos(3, 0.5, 100000)