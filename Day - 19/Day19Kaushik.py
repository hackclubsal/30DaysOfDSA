#Q19


#Determine if S can be broken down into a sequence of words where each word is an element in W
def wordCheck(w, s):
    if not s:
        return True
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        if prefix in w and wordCheck(w, s[i:]):
            return True
    return False       

w = ['tech', 'work', 'problem', 'at']
s = 'workattech'

res = wordCheck(w, s)
print(res)