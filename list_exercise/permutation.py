permutation = input().split()
sequence = int(input())
result = []

while len(permutation) > 0:
    if sequence > len(permutation):
        to_remove = permutation[sequence]
    permutation.pop(sequence)
    result.append(to_remove)
