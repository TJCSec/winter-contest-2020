def numerize(s):
	o = ''
	for c in s:
		if c in alpha:
			i = alpha.index(c)
		else:
			i = -1
		o += str(numero[i])
	return o

alpha = list('abcdefghijklmnopqrstuvwxyz')
numero = list(range(27))

# we lost the input file, sorry! you'll have to try and recreate it...
inp = open('input.txt', 'r').read().lower()
outp = open('output.txt', 'w')

outp.write(numerize(inp))
outp.write('\n')
outp.write(numerize(inp[::-1]))