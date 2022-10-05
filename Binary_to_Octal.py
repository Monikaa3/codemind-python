for i in range(int(input())):
    binnum=input()
    octnum=int(binnum,2)
    octnum=oct(octnum)
    print(octnum[2:])