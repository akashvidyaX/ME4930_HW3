import numpy as np

def is_rotation_matrix(R):
    """Check if a 3x3 matrix is a valid rotation matrix."""
    
    # Ensure the matrix is 3x3
    if R.shape != (3, 3):
        return False
    
    # Check if R * R^T is close to the identity matrix
    identity_matrix = np.eye(3)
    tolerance = 1e-5
    if not np.allclose(R @ R.T, identity_matrix, atol=tolerance):
        return False

    # Check if determinant is close to 1
    if not np.isclose(np.linalg.det(R), 1, atol=tolerance):
        return False
    
    return True

def rotation_matrix_x(theta):
    """Generate a rotation matrix for a rotation about the X-axis by theta."""
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

# Test the is_rotation_matrix function
if __name__ == "__main__":
    test_matrix = rotation_matrix_x(45 * np.pi / 180)
    print("Test Matrix:")
    print(test_matrix)
    print("\nIs Rotation Matrix? ", is_rotation_matrix(test_matrix))
