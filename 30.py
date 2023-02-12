d = {}
while inp := input():
	inp = ' '.join(inp.split())
	if len(inp) < len('class X:'):
		continue
	if inp[0:5] != 'class':
		continue
	d[inp[6]] = [inp[6]]
	if '(' not in inp:
		continue
	l = inp.split('(')
	l = l[1]
	l = l.split(')')
	l = l[0].replace(' ', '', len(l[0])).split(',')
	d[inp[6]] = d[inp[6]] + l
	
print(d)
print()
	
fl = 1
for key in d:
	lin = []
	print(d)
	l = [list(key)]
	for c in d[key]:
		if c == key:
			continue
		l.append(d[c])
	while l:
		for n in range(0, len(l)):
			for i in range(0, len(l)):
				if i == n:
					continue
				if l[n][0] in l[i] and l[n][0] != l[i][0]:
					break
			else:
				lin.append(l[n][0])
				elem = l[n][0]
				for lists in l:
					if elem in lists:
						lists.remove(elem)
				while [] in l:
					l.remove([])
				break
		else:
			print('No')
			fl = 0
	d[key] = list(lin)
	print(lin)
	print(d)

print()
print(d)	
if fl:
	print('Yes')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
