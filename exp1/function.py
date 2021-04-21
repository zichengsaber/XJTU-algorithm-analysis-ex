import random
import math
import numpy as np 

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle=[x for x in arr if x==pivot]
    return quicksort(left)+middle+quicksort(right)

# O(n) 中位数
class LinearSelection(object):
    def select(self,A,k):
        if len(A)==1:
            return A[0] #只有一个元素时第k小只能是A[0]
        p=self.medianOfMedian(A) #T(n/5)
        L,M,R=self.partition(A,p)# O(n)

        # T(7n/10)
        if len(L)<k and k<=len(M)+len(L):
            return p
        elif k<=len(L):
            return self.select(L,k)
        elif k>len(M)+len(L):
            return self.select(R,k-len(M)-len(L))
    
    def partition(self,A,pivot):
        L=[x for x in A if x<pivot]
        R=[x for x in A if x>pivot]
        M=[x for x in A if x==pivot]
        return L,M,R
    
    def medianOfMedian(self,A):
        median_arr=[]
        for i in range(0,len(A),5):
            k=min(i+5,len(A))
            arr=A[i:k].copy()
            arr=quicksort(arr)
            median_arr.append(arr[len(arr)//2])
        return self.select(median_arr,math.ceil(len(median_arr)//2))
    def findMedian(self,A):
        if len(A)%2==0:
            return (self.select(A,len(A)//2)+self.select(A,len(A)//2+1))/2
        else:
            return self.select(A,math.ceil(len(A)/2)) # ceil(n/2)

if __name__=='__main__':
    arr1=[random.randint(0,1000) for i in range(10)]
    arr2=[random.randint(0,1000) for i in range(9)]
    fun=LinearSelection()
    print("numpy.median:{}".format(np.median(arr1)))
    print("my algorithm:{}".format(fun.findMedian(arr1)))
    print("numpy.median:{}".format(np.median(arr2)))
    print("my algorithm:{}".format(fun.findMedian(arr2)))

    
