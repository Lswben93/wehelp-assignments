import numpy as np
def maxProduct(nums):
    a=[]
    for i in nums:
        for j in nums:
            if(i!=j):
                n=i*j                
                a.append(int(n))
    print(max(a))
maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])