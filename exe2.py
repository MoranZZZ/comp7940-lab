def find_factors(x):
    """return all factors"""
    print(f"{x} factors are:")
    
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    
    print(factors)
    print(f"has {len(factors)} factors")
    return factors

# using
x = 52633
find_factors(x)