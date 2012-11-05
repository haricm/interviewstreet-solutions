import sys
def pascal(n,r) :
	if r == 0 or r == n:
		return 1
	elif r == 1 or r == n -1:
		return n
	else :
		list=[]
		list2=[]
		for i in range(2, n - r +2):
			list.append(i)
		for i in range(2, r+1):
			for j in range(i+1, n + i +  1 -r):
#				print str(i) + " " + str(j)
				if j - i == 1:
					list2.append(list[0] + 1)
				else:
					list2.append(list2[j-i-2] + list[j-i-1])
			list=[l for l in list2]
			list2=[]		 
		return list.pop()


nooftestcases = int(raw_input())
for i in range(nooftestcases):
	temp = raw_input()
	[e, f] = [ int(x) for x in temp.split() ]
	if e - f < f:
		f = e - f
	result = pascal(e,f) 
	sys.stdout.write(str(result) + '\n')
	

