def hl(heads,legs):
    for chicken in range(heads+1):
        rabbit=heads-chicken
        if 2*chicken+4*rabbit==legs:
            return chicken,rabbit

heads=35
legs=94
print(hl(heads,legs))