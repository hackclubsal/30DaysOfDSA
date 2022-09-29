class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def sackval(W, arr):
    arr.sort(key=lambda x:(x.value/x.weight), reverse=True)
    finalvalue = 0
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
        else:
            finalvalue += item.value * W / item.weight
            break
    return finalvalue

W = 5
arr = [Item(1, 3), Item(2, 4), Item(3, 5), Item(4, 7)]

maxval = sackval(W, arr)
print("Max value : ", format(maxval))
