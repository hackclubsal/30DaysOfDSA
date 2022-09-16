inp_data = [each for each in input()]

while inp_data[0]=='/':

    temp=[]

    i=0

    n=0

    search=chr(92)

    while inp_data[i]!=search:

        temp.append(inp_data[i])

        if inp_data[i]=='/':

            n=i

        i=i+1

    inp_data=inp_data[:n]+inp_data[i-1:n:-1]+inp_data[i+1:]

print(''.join(inp_data))
