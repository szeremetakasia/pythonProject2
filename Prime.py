n = 100

print("First", n, "prime numbers are:")

for num in range(n):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
