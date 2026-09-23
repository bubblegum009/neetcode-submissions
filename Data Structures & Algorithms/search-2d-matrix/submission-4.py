class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        col=len(matrix[0])
        reqrow=0

        for i in range(0,rows):
            if matrix[i][0]<=target and matrix[i][col-1]>=target:
                reqrow=i

        arr=matrix[reqrow]
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False
