booksInp = input()
# booksInp = "/o\\/p\\/i/o/pp\\u\\"

i = 0

booksInp = booksInp.removeprefix("\\")
booksInp = booksInp.removesuffix("/")

print(booksInp)



while booksInp.__contains__('/') or booksInp.__contains__('\\'):
    if booksInp[i] == '\\':
        booksInp = booksInp.replace("\\", " ", 1)
    elif booksInp[i] == '/':
        booksInp = booksInp.replace("/", " ", 1)
    i+=1

a = list(reversed(booksInp.split(" ")))

b=""
for i in a:
    b += i
print(b)