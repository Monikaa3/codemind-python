def aq(h,sp,sf):
    if h>50 and sp>60 and sf>100:
        return ("10")
    elif h>50 and sp>60:
        return ("9")
    elif sp>60 and sf>100:
        return ("8")
    elif h>50 and sf>100:
        return ("7")
    elif h>50 or sp>60 or sf>100:
        return ("6")
    else:
        return ("5")
h,sp,sf=map(int,input().split())
print(aq(h,sp,sf))