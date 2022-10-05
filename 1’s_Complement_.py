import math
def onesComplement(n):
    num_of_bits=(int)(math.floor(math.log(n)/math.log(2)))+1;
    return ((1<<num_of_bits)-1)^n;
n=int(input())
print(onesComplement(n))