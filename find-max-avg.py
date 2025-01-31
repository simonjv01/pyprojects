def findMaxAvg(nums: list[int], k:int) -> float:
    # calculate the sum of the first k elements
    total_sum = sum(nums[:k])
    print(total_sum)

    # initialize the maximum sum to the sum of the first k elements
    max_sum = total_sum

    # iterate through the rest of the elements
    for i in range(k, len(nums)):
        # update the total sum by adding the current element and subtracting the first element
        total_sum += nums[i] - nums[i - k]
        print("in for loop", total_sum)

        #update the maximum sum
        max_sum = max(max_sum, total_sum)
    # return the maximum average
    return max_sum / k

nums = [1, 12, -5, -6, 50, 3]
k = 4
result = findMaxAvg(nums, k)
print(result) # Output: 12.75
