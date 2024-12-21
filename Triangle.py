def mirrored_right_angled_triangle(n):
    for i in range(1, n + 1):
        # Print spaces first, then stars
        print(' ' * (n - i) + '*' * i)

# Test the function with n = 5
mirrored_right_angled_triangle(20)
