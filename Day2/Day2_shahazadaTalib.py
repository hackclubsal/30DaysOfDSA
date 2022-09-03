
class RotateArray():

    def __init__(self,arr,k) -> None:
        self.arr=arr
        self.k=k
        self.n=len(arr)

    def rotateArrayByK(self):
        arr[:] = arr[self.k%self.n:self.n] + arr[0:self.k%self.n]
        return arr

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7]
    k=3

    obj = RotateArray(arr,k)

    arr=obj.rotateArrayByK()
    print(arr)

    

