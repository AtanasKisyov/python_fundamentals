n = int(input())
is_prime = True
for i in range(2 , n):
    if n % i == 0:
        is_prime = False
print(is_prime)
