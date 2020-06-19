def isprime(n):
	factors = []
	if (n>1):
		floor_sqrt = int(n ** (0.5))
		for d in range(2,floor_sqrt + 1):
			if n % d != 0:
				continue
			factors.append(d)
			n = n/d

		if len(factors) == 0:
			return True
	return False

