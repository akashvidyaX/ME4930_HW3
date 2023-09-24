import numpy as np
import matplotlib.pyplot as plt

# Frame {s} is our standard frame, so its x, y, z axes are just the unit vectors
s_x = [1, 0, 0]
s_y = [0, 1, 0]
s_z = [0, 0, 1]

# For frame {a}
a_x = [0, 0, 1]
a_y = [-1, 0, 0]
a_z = np.cross(a_x, a_y)  # Using right-hand rule

# For frame {b}
b_x = [1, 0, 0]
b_y = [0, 0, -1]
b_z = np.cross(b_x, b_y)  # Using right-hand rule

# Plotting the frames
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot frame {s}
ax.quiver(0, 0, 0, *s_x, color='r', label='s_X-axis')
ax.quiver(0, 0, 0, *s_y, color='g', label='s_Y-axis')
ax.quiver(0, 0, 0, *s_z, color='b', label='s_Z-axis')

# Plot frame {a} - shifted for visualization
ax.quiver(2, 2, 2, *a_x, color='r', linestyle='dashed', label='a_X-axis')
ax.quiver(2, 2, 2, *a_y, color='g', linestyle='dashed', label='a_Y-axis')
ax.quiver(2, 2, 2, *a_z, color='b', linestyle='dashed', label='a_Z-axis')

# Plot frame {b} - shifted for visualization
ax.quiver(-2, -2, -2, *b_x, color='r', linestyle='dotted', label='b_X-axis')
ax.quiver(-2, -2, -2, *b_y, color='g', linestyle='dotted', label='b_Y-axis')
ax.quiver(-2, -2, -2, *b_z, color='b', linestyle='dotted', label='b_Z-axis')

# Set plot appearance
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.view_init(30, 30)  # Adjust viewing angle for better visualization

plt.title("Visualization of frames {s}, {a}, and {b}")
plt.show()
