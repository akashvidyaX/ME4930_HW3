import numpy as np
np.set_printoptions(suppress=True)

# Define the rotation matrix for x-axis rotation
def rotation_matrix_x(theta):
    """Generate a rotation matrix for a rotation about the X-axis by theta."""
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

# Define the matrices for frames {a} and {b} w.r.t. frame {s}
x_a = [0, 0, 1]
y_a = [-1, 0, 0]
z_a = np.cross(x_a, y_a)
R_s_a = np.column_stack((x_a, y_a, z_a))

x_b = [1, 0, 0]
y_b = [0, 0, -1]
z_b = np.cross(x_b, y_b)
R_s_b = np.column_stack((x_b, y_b, z_b))

# Defining the rotation of -90 degrees about x-axis
theta = -90 * np.pi / 180
R = rotation_matrix_x(theta)

# Calculating R1 and R2
R1 = R_s_a @ R
R2 = R @ R_s_a

print(R)

print(R_s_a)
print(R_s_b)

print(R1)
print(R2)

import matplotlib.pyplot as plt

def plot_3d_frame_with_offset(matrix, ax, offset, color, label=''):
    """Visualize the 3D frame described by the matrix with an offset."""
    origin = np.array(offset)
    x_axis, y_axis, z_axis = matrix[:, 0], matrix[:, 1], matrix[:, 2]
    ax.quiver(*origin, *x_axis, color=color[0], label=f'X-{label}')
    ax.quiver(*origin, *y_axis, color=color[1], label=f'Y-{label}')
    ax.quiver(*origin, *z_axis, color=color[2], label=f'Z-{label}')

# Set up the plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the original frame {s} with offset [0, 0, 0]
plot_3d_frame_with_offset(np.eye(3), ax, [0, 0, 0], ['r', 'g', 'b'], label='s')

# Plot the frame {a} with offset [-1, 1, 0]
plot_3d_frame_with_offset(R_s_a, ax, [-1, 1, 0], ['m', 'y', 'c'], label='a')

# Plot the new orientations R1 with offset [1, 1, 0]
plot_3d_frame_with_offset(R1, ax, [1, 1, 0], ['#FF4500', '#7FFF00', '#1E90FF'], label='R1')

# Plot the new orientations R2 with offset [0, -1, 0]
plot_3d_frame_with_offset(R2, ax, [0, -1, 0], ['#8B008B', '#556B2F', '#8B4513'], label='R2')

# Set the plot limits and labels
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend(loc='upper left')

plt.title("Visualization of Frames and Orientations with Offsets")
plt.show()

# Given point p_b in {b} coordinates
p_b = np.array([1, 2, 3])

# Transforming the point to {s} coordinates using R_s_b (the rotation matrix from frame {b} to frame {s})
p_s = R_s_b @ p_b

print(R_s_b)
print(p_b)
print(p_s)

# Given point p_s in {s} coordinates
p_s = np.array([1, 2, 3])

# Calculating p' and p''
p_prime = R_s_b @ p_s
p_double_prime = np.transpose(R_s_b) @ p_s

print(p_prime, p_double_prime)
