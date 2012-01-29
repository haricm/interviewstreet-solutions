import sys
t = int ( raw_input() )
for i in range(t):
	n, m = [int(x) for x in raw_input().split()]
	result = (pow(2,n+1)-pow(2,m+1))
	sys.stdout.write(str(result) + ".00\n") 
