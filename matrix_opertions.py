import numpy as np

def transpose_matrix(matrix):
    """Returns the transpose of the given matrix."""
    return np.transpose(matrix)

def inverse_matrix(matrix):
    """Returns the inverse of the given matrix."""
    return np.linalg.inv(matrix)

def multiply_matrices(matrix1, matrix2):
    """Returns the product of the two given matrices."""
    return np.dot(matrix1, matrix2)

# Example Usage:
if __name__ == "__main__":
    A = np.array([[1, 0, 0], [0, 0.525, 0.85], [0, -0.85, 0.525]])
    B = np.array([[0.525, -0.85, 0], [0.85, 0.525, 0], [0, 0, 1]])
    
    print("Matrix A:")
    print(A)

    print("Matrix B:")
    print(B)

    print("\nMultiplication of A and B:")
    print(multiply_matrices(A, B))

    