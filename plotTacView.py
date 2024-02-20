import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def ru_plot_data_file(ax, file_path):
    # Read data from the file
    data = []
    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split(",")
            data.append([float(value) for value in values[:3]])

    # Separate x, y, and z values from the data
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    z = [point[2] for point in data]

    # Create the scatter plot
    ax.scatter(x, y, z,s=2,color = 'red')

def us_plot_data_file(ax, file_path):
    # Read data from the file
    data = []
    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split(",")
            data.append([float(value) for value in values[:3]])

    # Separate x, y, and z values from the data
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    z = [point[2] for point in data]

    # Create the scatter plot
    ax.scatter(x, y, z,s=2,color = 'blue')


# File paths
ru_file_paths = [
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/101.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/201.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/301.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/401.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/501.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/601.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/701.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/801.txt",
]

us_file_paths = [
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/1001.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/1001.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/a01.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/b01.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/c01.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/e01.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/f01.txt",
    "/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/b01.txt",
]

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot data from each file on the same plot
for file_path in ru_file_paths:
    ru_plot_data_file(ax, file_path)

for file_path in us_file_paths:
    us_plot_data_file(ax, file_path)

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()