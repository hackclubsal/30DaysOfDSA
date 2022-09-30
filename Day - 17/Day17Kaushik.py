/*Q.17) You are given two strings s1 and s2. Find the minimum number of operations required to convert s1 to s2.
Permitted Operations:
1: Insert a character

2: Delete a character

3: Replace a character

4: Strings s1 and s2 are composed of only lowercase English characters.

Example:-

Input:
s1: "hello"

s2: "seldom"

Output:
Result: 3

Explanation:
hello → sello (replace h with s)

sello → seldo (replace l with d)

seldo → seldom (insert m at end)*/


import sys
 


def minimumChar(S1, S2):
     
    
    n, m = len(S1), len(S2)
 
    ans = sys.maxsize
 
    
    for i in range(m - n + 1):
        minRemovedChar = 0
 
        
        
        
        for j in range(n):
            if (S1[j] != S2[i + j]):
                minRemovedChar += 1
                 
        
        
        ans = min(minRemovedChar, ans)
         
    
    return ans
     

if __name__ == '__main__':
    S1 = "hello"
    S2 = "seldom"
    print(minimumChar(S1, S2))