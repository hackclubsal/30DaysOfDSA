

class FindKey():

    def __init__(self,matrix,key) -> None:
        self.matrix=matrix
        self.key=key
        self.n=len(matrix[0])
        self.m=len(matrix)

    def searchKey(self):
        lft=0
        rgt=self.m*self.n-1

        while(lft<=rgt):
            mid=lft+(rgt-lft)//2

            if(self.matrix[mid//self.n][mid%self.n]==self.key):
                return True
            elif(self.matrix[mid//self.n][mid%self.n]>self.key):
                rgt=mid-1
            else:
                lft=mid+1
                
        return False

        

if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    key=1

    obj = FindKey(matrix,key)

    get=obj.searchKey()
    print(get)

    

