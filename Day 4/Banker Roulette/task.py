import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

val = random.randint(0, len(friends)-1)
print(friends[val])
print(random.choice(friends))