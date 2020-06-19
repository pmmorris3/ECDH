import math

def tobinary(n):
	while(n>=0):
		i = 0
		if n==0:
			return n
		binary_digits = []
		r = int(math.log(n,2))
		for l in range(0,r+1):
			if n % 2 == 1:
				binary_digits.append(1)
				n=int(n/2)
			else:
				binary_digits.append(0)
				n=int(n/2)
		return binary_digits
		break


if __name__ == "__main__":
	n=int(input("Enter a number n."))
	tobinary(n)