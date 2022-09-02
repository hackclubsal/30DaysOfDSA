'''
[1,0,1,0,0,1,1,0]

'''
class SortBinaryArray:
    
    def __init__(self,arr):
        self.arr = arr
        self.n = len(arr)

    def sortBinaryArray(self):
        zeroPtr=0
        onePtr=len(arr)-1
        while(onePtr>zeroPtr):
            if(arr[zeroPtr]==0):
                zeroPtr+=1
            if(arr[onePtr]==1):
                onePtr-=1
            else:
                arr[zeroPtr],arr[onePtr]=arr[onePtr],arr[zeroPtr]
     
    def displayArray(self):
        print(self.arr)
    
        

if __name__=="__main__":
    
#     inpt=input("anter array: ")
#     arr=[int(i) for i in inpt.split(',')]

    arr = [1, 0, 1, 0, 1, 0, 0, 1]
    obj = SortBinaryArray(arr)
    obj.sortBinaryArray()
    obj.displayArray()



