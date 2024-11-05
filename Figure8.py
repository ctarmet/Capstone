import numpy as np
import matplotlib.pyplot as plt

def penta():
    l = np.sqrt(200**2/(2*(1-np.cos(2*np.pi/5))))
    vertices = np.array([[l*np.cos(np.pi/10),l*np.sin(np.pi/10)], [l*np.cos(np.pi/10 + 2*np.pi/5),l*np.sin(np.pi/10 + 2*np.pi/5)], [l*np.cos(np.pi/10 + 4*np.pi/5),l*np.sin(np.pi/10 + 4*np.pi/5)], [l*np.cos(np.pi/10 + 6*np.pi/5),l*np.sin(np.pi/10 + 6*np.pi/5)], [l*np.cos(np.pi/10 + 8*np.pi/5),l*np.sin(np.pi/10 + 8*np.pi/5)]])

    return vertices

def penta2():
    l = np.sqrt(200**2/(2*(1-np.cos(2*np.pi/5))))
    phi = (np.sqrt(5) + 1)/2
    x = 200 * phi
    vertices2 = np.array([[l*np.cos(np.pi/10) + x,l*np.sin(np.pi/10)], [l*np.cos(np.pi/10 + 2*np.pi/5) + x,l*np.sin(np.pi/10 + 2*np.pi/5)], [l*np.cos(np.pi/10 + 4*np.pi/5) + x,l*np.sin(np.pi/10 + 4*np.pi/5)], [l*np.cos(np.pi/10 + 6*np.pi/5) + x,l*np.sin(np.pi/10 + 6*np.pi/5)], [l*np.cos(np.pi/10 + 8*np.pi/5) + x,l*np.sin(np.pi/10 + 8*np.pi/5)]])

    return vertices2

def plot():
    vertices = penta()
    vertices2 = penta2()
    plt.plot([vertices[0][0], vertices[1][0]], [vertices[0][1], vertices[1][1]], 'k-')
    plt.plot([vertices[1][0], vertices[2][0]], [vertices[1][1], vertices[2][1]], 'k-')
    plt.plot([vertices[2][0], vertices[3][0]], [vertices[2][1], vertices[3][1]], 'k-')
    plt.plot([vertices[3][0], vertices[4][0]], [vertices[3][1], vertices[4][1]], 'k-')
    plt.plot([vertices[0][0], vertices[4][0]], [vertices[0][1], vertices[4][1]], 'k-')
    plt.plot([vertices[2][0], vertices[0][0]], [vertices[2][1], vertices[0][1]], 'r-')

    plt.plot([vertices2[0][0], vertices2[1][0]], [vertices2[0][1], vertices2[1][1]], 'k-')
    plt.plot([vertices2[1][0], vertices2[2][0]], [vertices2[1][1], vertices2[2][1]], 'k-')
    plt.plot([vertices2[2][0], vertices2[3][0]], [vertices2[2][1], vertices2[3][1]], 'k-')
    plt.plot([vertices2[3][0], vertices2[4][0]], [vertices2[3][1], vertices2[4][1]], 'k-')
    plt.plot([vertices2[0][0], vertices2[4][0]], [vertices2[0][1], vertices2[4][1]], 'k-')

    plt.plot([vertices[3][0], vertices2[4][0]], [vertices[3][1], vertices2[4][1]], 'b-')

    plt.axis('equal')
    plt.axis('off')
    plt.show()


plot()