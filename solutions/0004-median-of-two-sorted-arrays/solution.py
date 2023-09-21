class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       l=[]
       j=0
       s=0
       i=0
       l=nums1+nums2
       l.sort()
       if(len(l)%2==1):
          j=(len(l)//2)
          for i in range(len(l)):
             if(i==j):
                return (float(l[i]))
       else:
           j=(len(l)//2)
           k=j-1
           for i in range(len(l)):
              if(i==j or i==k):
                s=s+l[i]
           return (float(s/2))
  
        
