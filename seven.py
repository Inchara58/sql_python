def matrix_traverse(mat):
    if not mat:
        return []
    
    rows, cols = len(mat), len(mat[0])
    
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    
    result = []
    
    while top <= bottom and left <= right:
        
        # Left → Right
        for j in range(left, right + 1):
            result.append(mat[top][j])
        top += 1
        
        # Top → Bottom
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        
        # Right → Left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(mat[bottom][j])
            bottom -= 1
        
        # Bottom → Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    
    return result


# 🔹 Matrix Input
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]

# 🔹 Function Call
print("Spiral Order:", matrix_traverse(matrix))