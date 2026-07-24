
numbers = [1, 2, 3, 4, 5, 6,7,7,6]

counts = {"even": 0, "odd": 0}

for num in numbers:
    if num % 2 == 0:
        counts["even"] += 1
    else:
        counts["odd"] += 1

print(f"Even: {counts['even']}")
print(f"Odd: {counts['odd']}")