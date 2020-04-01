import sys
 
inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        result = a+b
        print("Case #%s: %s + %s = %s"%(i+1,a,b,result))