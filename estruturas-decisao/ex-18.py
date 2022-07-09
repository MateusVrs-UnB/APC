def pitorestico(a, b, c):
	final = map(lambda x: x%2 + x%3 + x%5, [a, b, c])
	print('Pitorestico!!!' if not any(final) else 'Nao foi dessa vez')