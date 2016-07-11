def d(x):
	x = x[::-1]#reversing the list x
	n = 0#will be the output
	exp = 0#power of ten that items in reversed x are multiplied by
	for i in x:#takes items in reversed x, adds them(multiplied by powers of ten) to n 
		n += i*(10**exp)
		exp += 1
	return n
print(d([1,7,2,9]))