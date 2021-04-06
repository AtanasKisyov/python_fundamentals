n = int(input())
pool = 0

for i in range(n):
    bucket = int(input())
    if pool + bucket > 255:
        print('Insufficient capacity!')
    else:
        pool += bucket
print(pool)
