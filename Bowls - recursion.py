# method 1

rows = 4
balls = rows

while rows > 0:
    balls = balls + rows - 1
    rows = rows - 1

print(balls)


# recursion method

def sum_bowls(n):
    if n == 1:
        return n
    else:
        return n + sum_bowls(n - 1)


print(sum_bowls(4))
