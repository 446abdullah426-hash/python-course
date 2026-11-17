n = 5
total = n * (n + 1) // 2
print("Sum =", total)


n = 5
total = 0
for i in range(1, n + 1):
    total = total + i
    print("Sum =", total)


n = 5
total = 0
steps = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        total = total + i
        steps = steps + 1
        print("Step =", steps)
print("Sum =", total // n)
