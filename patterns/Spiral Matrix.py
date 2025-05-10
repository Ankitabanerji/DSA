def generate_spiral_matrix(n):
    # Create an n x n matrix initialized with 0s
    matrix = [[0] * n for _ in range(n)]

    num = 1  # Start filling with 1
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while num <= n * n:
        # Fill the top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Fill the right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Fill the bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Fill the left column
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print("  ".join(f"{num:2d}" for num in row))


# Example usage
n = 5
spiral_matrix = generate_spiral_matrix(n)
print_matrix(spiral_matrix)
