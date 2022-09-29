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
