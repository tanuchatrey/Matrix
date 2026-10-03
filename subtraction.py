# Subtraction of two matrices

A = [
    [10, 20, 30],
    [40, 50, 60]
]

B = [
    [1, 2, 3],
    [4, 5, 6]
]

# Create result matrix
result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] - B[i][j])
    result.append(row)

# Display result
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nSubtraction of matrices:")
for row in result:
    print(row)
