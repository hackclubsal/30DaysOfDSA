def ops(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return ops(str1, str2, m-1, n-1)
    return 1 + min(ops(str1, str2, m, n-1), # Insert
                ops(str1, str2, m-1, n), # Remove
                ops(str1, str2, m-1, n-1) # Replace
                )

str1 = "hello"
str2 = "seldom"
print (ops(str1, str2, len(str1), len(str2)))
