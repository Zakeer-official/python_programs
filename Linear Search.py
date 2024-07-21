
def search(nums,ele):
    for i in nums:
        if i == ele:
            return True
    return False


    
#Example:
nums = [1,5,8,3,2,7,4]
ele = 2

print(search(nums,ele))
