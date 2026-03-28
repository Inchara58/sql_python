def single_number(nums):
    # Step 1: Initialize result
    result = 0
    
    # Step 2: Traverse the array
    for num in nums:
        result = result ^ num   # XOR operation
    
    # Step 3: Return the unique element
    return result


# 🔹 Example usage
nums = [4, 1, 2, 1, 2]
print("Single number is:", single_number(nums))