def has_33(nums):
    OK = False
    for i in range(len(nums)):
        if i + 1 != len(nums) and nums[i] == nums[i + 1] and nums[i] == 3:
            OK = True
    print(True) if  OK == True else print(False) 

has_33([1, 3, 3]) 
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 