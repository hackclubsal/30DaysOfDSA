def wordBreak(words, word):
    
    if not word:
        return True
 
    for i in range(1, len(word) + 1):
        
        prefix = word[:i]
        
        if prefix in words and wordBreak(words, word[i:]):
            return True
    
    return False

if __name__ == '__main__':
   
    words = [
       'tech', 'work', 'problem', 'at' ]
     
    word = 'workattech'
 
    if wordBreak(words, word):
        print('True')
    else:
        print('False')
