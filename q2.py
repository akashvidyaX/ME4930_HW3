import numpy as np
np.set_printoptions(suppress=True)

p = np.array([1/np.sqrt(3), -1/np.sqrt(6), 1/np.sqrt(2)])

# Define the rotation matrices for rotations about x, y, and z axes

def rotation_matrix_x(theta):
    """Generate a rotation matrix for a rotation about the X-axis by theta."""
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

def rotation_matrix_y(theta):
    """Generate a rotation matrix for a rotation about the Y-axis by theta."""
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def rotation_matrix_z(theta):
    """Generate a rotation matrix for a rotation about the Z-axis by theta."""
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

# Redefining the rotation matrices for the given angles
R_x = rotation_matrix_x(30 * np.pi / 180)  # Rotation about x-axis by 30 degrees
R_y = rotation_matrix_y(135 * np.pi / 180)  # Rotation about y-axis by 135 degrees
R_z = rotation_matrix_z(-120 * np.pi / 180)  # Rotation about z-axis by -120 degrees

# Apply the rotations to the point p
p_prime = R_z @ R_y @ R_x @ p
print(R_x)
print(R_y)
print(R_z)

print(p)
print(p_prime)
