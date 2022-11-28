def reverseint(x):
    y=list(str(x))
    z=reversed(y)
    k="".join(z)
    t=int(k)
    return t

nums=list(range(0,100001))
print("the special numbers from 0 to 100000 are :")
for i in range (0,len(nums)):
    if nums[i]*4==reverseint(nums[i]):
        q=nums[i]
        print(q)
