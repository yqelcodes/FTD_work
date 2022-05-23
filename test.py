def movezeroes(nums):
    l = 0 
    for i in range(len(nums)):
        if nums[i]:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
    return nums


a = [1,0,0,3,0,4,5,9,0]
print(movezeroes(a))