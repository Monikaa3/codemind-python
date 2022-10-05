def octtobin(o):
    return bin(int(o,8))
for i in range(int(input())):
    octnum=input()
    binnum=octtobin(octnum)
    print(binnum[2:])