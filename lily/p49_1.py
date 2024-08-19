nums=list(range(3))
# nums+=[100,10]
nums.extend(([100,10]))
print(nums)
print(len(nums))
nums.sort()
print(nums)