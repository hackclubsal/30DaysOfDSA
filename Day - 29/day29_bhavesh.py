
def ispalindrome(s):
 
    l = len(s)
     
    i = 0
    j = l - 1
    while i <= j:
     
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
     
    return True
 

if __name__ == "__main__":
     
    s = "BAABA"
    cnt = 0
    flag = 0
     
    while(len(s) > 0):
     
        
        if(ispalindrome(s)):
            flag = 1
            break
         
        else:
            cnt += 1
         
            
            s = s[:-1]
     
    
    if(flag):
        print(cnt)

def computeLPSArray(string):
 
    M = len(string)
    lps = [None] * M
 
    length = 0
    lps[0] = 0 
 
    
    
    i = 1
    while i < M:
     
        if string[i] == string[length]:
         
            length += 1
            lps[i] = length
            i += 1
         
        else: 
         
            
            
            
            if length != 0:
             
                length = lps[length - 1]
 
                
                
             
            else: 
             
                lps[i] = 0
                i += 1
 
    return lps
 



def getMinCharToAddedToMakeStringPalin(string):
 
    revStr = string[::-1]
 
    
    
    concat = string + "$" + revStr
 
    
    
    lps = computeLPSArray(concat)
 
    
    
    
    return len(string) - lps[-1]
 

if __name__ == "__main__":
 
    string = "AACECAAAA"
    print(getMinCharToAddedToMakeStringPalin(string))

