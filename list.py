if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    permutation = [[a, b, c] for a in range(x + y + z + 1) if a <= x for b in range(y + x + z + 1) if b <= y \
                            for c in range(z + x + y + 1) if c <= z if a + b + c != n]
    print(permutation)