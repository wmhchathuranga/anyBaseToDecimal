import sys

def anyTodecimalconvert(a=157,b=10):

	aStr = [str(a)[i] for i in range(len(str(a))-1,-1,-1)]
	if(all([int(i)<b for i in aStr])):
		print(f'\n{a}\n')
		print(' + '.join([f'{aStr[i]}*{b}^{i}' for i in range(len(str(a))-1,-1,-1)]))
		print(' + '.join([f'{aStr[i]}*{b**i}' for i in range(len(str(a))-1,-1,-1)]))
		print(' + '.join([str(int(aStr[i])*b**i) for i in range(len(str(a))-1,-1,-1)]))
		print('\n=',(sum([int(f'{int(aStr[i])*b**i}') for i in range(len(str(a))-1,-1,-1)])))
		print()
	else:
		print(f'\n[!] {a} is not valid for base {b}\n')

try:
	anyTodecimalconvert(int(sys.argv[1]),int(sys.argv[2]))
except:
	print("\n\n------------Usage----------- \n\n python .\\ToDecimal.py <number> <base>\n\n")