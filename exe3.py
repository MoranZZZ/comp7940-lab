def get_factors(n):
    """return all the factors"""
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors

# list
l = [52633, 8137, 1024, 999]

for num in l:
    factors = get_factors(num)
    print(f"{num} factors are: {factors}")
    print(f"Total: {len(factors)} factors\n")