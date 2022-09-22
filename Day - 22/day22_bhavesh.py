def isConsecutive(strs):
   
    
    start = 0;
 
    
    length = len(strs);
 
    
    for i in range(length // 2):
 
        
       
        new_str = strs[0: i + 1];
 
        
        num = int(new_str);
 
        
        start = num;
 
        
        
        while (len(new_str) < length):
            
            num += 1;
 
            
            new_str = new_str + str(num);
 
        
        
        if (new_str==(strs)):
            return start;
 
    
    return -1;
 

if __name__ == '__main__':
    str0 = "10099989796";
    print("String: " + str0);
    start = isConsecutive(str0);
    if (start != -1):
        print("Yes \n" , start);
    else:
        print("No");
 
    str1 = "54320";
    print("\nString: " , str1);
    start = isConsecutive(str1);
    if (start != -1):
        print("Yes \n" , start);
    else:
        print("No");
