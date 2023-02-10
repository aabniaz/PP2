def spy_game(nums):
    OK = False
    for i in range(len(nums)):
        if i + 1 != len(nums) and nums[i] == nums[i + 1] == 0 and nums[i + 2] == 7:
            OK = True
    print(True) if OK == True else print(False)

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 