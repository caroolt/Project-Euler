# 
# Solução para o problema 128 do Projeto Euler

import eulerlib, itertools

def compute():
	TARGET = 2000 
	count = 2  
	for ring in itertools.count(2):
		if all(map(eulerlib.is_prime, (ring * 6 - 1, ring * 6 + 1, ring * 12 + 5))):
			count += 1
			if count == TARGET:
				return str(ring * (ring - 1) * 3 + 2)
		if all(map(eulerlib.is_prime, (ring * 6 - 1, ring * 6 + 5, ring * 12 - 7))):
			count += 1
			if count == TARGET:
				return str(ring * (ring + 1) * 3 + 1)


if __name__ == "__main__":
	print(compute())