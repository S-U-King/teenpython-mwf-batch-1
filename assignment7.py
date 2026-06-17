# Print Numbers Except Multiples of 5
# Create a loop from 1 to 50.

# Print every number except the numbers divisible by 5.

# Example Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# ...

# 1 se 50 tak loop
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)
