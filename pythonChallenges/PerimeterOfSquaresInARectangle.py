def perimeter(n):
    squares = [1, 1]
    for c in range(n-1):
        squares.append(squares[c]+squares[c+1])
    return (n-(n-4))*sum(squares)

print(perimeter(7))