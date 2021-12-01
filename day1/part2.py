def main():
    list = inputAsList()
    res = 0
    for i in range (0,len(list)):
        if(sum(list[i:i+3]) < sum(list[i+1:i+4])):
            res+=1
    return res

def inputAsList():
    f = open('input')
    return list(map(int, f.read().splitlines()))

print(main())