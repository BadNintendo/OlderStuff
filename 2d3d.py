import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plot_octahedron(ax, center, size, label):
    # Define vertices of a unit octahedron centered at origin
    vertices = np.array([
        [1, 0, 0], [-1, 0, 0],
        [0, 1, 0], [0, -1, 0],
        [0, 0, 1], [0, 0, -1]
    ]) * size
    
    # Move to center position
    vertices += np.array(center)
    
    # Define the 8 triangular faces
    faces = [
        [vertices[0], vertices[2], vertices[4]],
        [vertices[0], vertices[2], vertices[5]],
        [vertices[0], vertices[3], vertices[4]],
        [vertices[0], vertices[3], vertices[5]],
        [vertices[1], vertices[2], vertices[4]],
        [vertices[1], vertices[2], vertices[5]],
        [vertices[1], vertices[3], vertices[4]],
        [vertices[1], vertices[3], vertices[5]]
    ]
    
    # Plot the faces
    ax.add_collection3d(Poly3DCollection(faces, color='skyblue', alpha=0.5, edgecolors='b'))
    ax.text(center[0], center[1], center[2], label, fontsize=12, ha='center', va='center')

def main():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    size = 1.5  # Size of each octahedron
    centers = [
        (-3, 3, 0), (3, 3, 0),
        (-3, -3, 0), (3, -3, 0)
    ]
    labels = ['Octahedron 1', 'Octahedron 2', 'Octahedron 3', 'Octahedron 4']
    
    for center, label in zip(centers, labels):
        plot_octahedron(ax, center, size, label)
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)
    ax.set_aspect('auto')
    ax.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
