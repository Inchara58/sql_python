def count_subarrays(arr, k):
    prefix_sum = 0
    count = 0
    
    # Dictionary to store prefix sum frequencies
    prefix_count = {0: 1}
    
    for num in arr:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]
        
        # Store prefix_sum
        if prefix_sum in prefix_count:
            prefix_count[prefix_sum] += 1
        else:
            prefix_count[prefix_sum] = 1
    
    return count


# Example
arr = [1, 2, 3, -2, 5]
k = 5

print("Number of subarrays:", count_subarrays(arr, k))