def maxZeros(nums):
    maxtime=0
    currecttime=0
    for i in nums:
        if i == 0:
            currecttime+=1
            maxtime=max(currecttime,maxtime)
        else:
            currecttime=0
    print(maxtime)
            

maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])
maxZeros([0,0,0,1,1])