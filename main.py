elements = [1000000000000, 2000000000, 1500000000]  # Example elements

# Summing elements using a 32-bit integer
total = sum(elements)  # Potential overflow may occur

# Summing elements using a 64-bit integer
total_64bit = sum(map(int, elements))  # No overflow concerns

print("Sum using 32-bit integer:", total)
print("Sum using 64-bit integer:", total_64bit)
