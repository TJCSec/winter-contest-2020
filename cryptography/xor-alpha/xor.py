flag = open('flag.txt').read().strip()

# converts flag to hex
hlag = flag.encode().hex()

# converts hex to int
ilag = int(hlag, 16)

# length of flag
llag = len(flag)

for c in 'abcdefghijklmnopqrstuvwxyz':
	long_char = c * llag
	hong_char = long_char.encode().hex()
	iong_char = int(hong_char, 16)
	ilag = ilag ^ iong_char

open('output.txt', 'w').write(str(ilag))
