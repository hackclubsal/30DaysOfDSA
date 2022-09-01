'''
[1,0,1,0,0,1,1,0]

'''

def sortBinaryArray(arr):
    
    zeroPtr=0
    onePtr=len(arr)-1
    while(onePtr>zeroPtr):
        if(arr[zeroPtr]==0):
            zeroPtr+=1
        if(arr[onePtr]==1):
            onePtr-=1
        else:
            arr[zeroPtr],arr[onePtr]=arr[onePtr],arr[zeroPtr]
    
        

if __name__=="__main__":
    
    inpt=input("anter array: ")

    arr=[int(i) for i in inpt.split()]
    sortBinaryArray(arr)
    print(arr)



