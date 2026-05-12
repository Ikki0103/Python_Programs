# bubble sort
def my_sort(nums):
    for i in range(len(nums)):          # outer loop - how many passes
        for j in range(len(nums) - 1):  # inner loop - compare neighbors
            if nums[j] < nums[j+1]:     # if left is smaller than right...
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


print(my_sort([3, 1, 4, 1, 5, 9, 2, 6]))

# Examples:
# my_sort([3, 1, 4, 1, 5, 9, 2, 6]) → [9, 6, 5, 4, 3, 2, 1, 1]
# my_sort([10, 3, 7, 2])             → [10, 7, 3, 2]
