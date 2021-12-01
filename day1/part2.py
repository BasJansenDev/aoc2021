def main():
    list = inputAsList()
    res = 0
    for i in range (0,len(list)-3):
        if(list[i] < list[i+3]):
            res+=1
    return res

def oneliner():
    return len(list(filter(lambda x: (x > 0),[j-i for i,j in zip(inputAsList()[:-1],inputAsList()[3:])])))

def inputAsList():
    f = open('input')
    return list(map(int, f.read().splitlines()))

print(main())
print(oneliner())