# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(10000)
lookup = {}
def pascal(n,r) :
    if r == 0 or r == n:
        return 1
    elif r == 1:
        return n
    elif (n,r) in lookup:
        return lookup[(n,r)]
    else:
		result1 = pascal(n-1,r-1) 
		result2 = pascal(n-1,r)
		result = result1 + result2
		lookup[(n,r)] = result
		print str(n) + "C" + str(r) + "=" + str(n-1) + "C"+ str(r) + "+"+ str(n-1) + "C"+ str(r-1) + "=" + str(result1) + "+"+ str(result2) + "="+ str(result) 
		return result
    
#t = int ( raw_input() )
t = 1
for i in range(t):
    [n, r] = [int(x) for x in raw_input().split()]
    sys.stdout.write(str(pascal(n,r)) + '\n')

