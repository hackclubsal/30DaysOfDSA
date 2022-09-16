#Sample Input: /u/love\i\   Sample Output: iloveu
a = "/u/love\\i\\"
a = a[1:-1]
a = a.replace("/", " ")
a = a.replace("\\", " ")
li = list(a.split(" "))
li.reverse()
res = ' '.join(map(str, li))
res = res.replace(" ", "")
print(res)
