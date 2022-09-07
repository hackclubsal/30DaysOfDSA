class Stack:

    def __init__(self):

        self.s=[]

        self.f=[]

    def lib(self,x):

        for i in range(len(x)+1):
            
            if x[i].isalpha():
                self.s.append(x[i])
            elif x[i]=='/':
                self.s.append(x[i])
            elif x[i]=='\\':
                while self.s[i]!='/' and len(self.s)>0:
                    self.f.append(self.s.pop())

                return self.f             

if __name__=='__main__':

    x="/u/love\\i\\"

    x=list(x)

    print(x[:])

    d=Stack()

    print(d.lib(x)) 
