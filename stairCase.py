def staircase(n):
    for i in range(1, n + 1):
        # Calculate the number of spaces and # symbols
        spaces = n - i
        symbols = i
        # Print spaces first
        print(" " * spaces, end="")
        # Print # symbols
        print("#" * symbols)

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
