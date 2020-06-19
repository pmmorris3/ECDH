"""
A point in the group and the order of the group (in this case the number of points on the elliptic curve) are public knowledge.

Bob chooses a secret message (a number b with 0 < b < n).
Alice chooses a secret message (a number a with 0 < a < n).

"""

from math import log
import random
import subprocess
from elliptic_curve import EllipticCurve


def encrypt(message, exchanged_value):
	"""
	A dumb way to encrypt a message
	"""
	encrypted_message = []
	for char in message:
		encrypted_message.append(ord(char)*exchanged_value[0])
	return encrypted_message


def decrypt(encrypted, exchanged_value):
	message = []
	for char in encrypted:
		val = int(char/exchanged_value[0])
		message.append(chr(val))
	return ''.join(str(e) for e in message)

if __name__ == "__main__":

	print("The elliptic curve we're working over is (modulo 115792089237316195423570985008687907853269984665640564039457584007908834671663):")
	ec = EllipticCurve(0,7,115792089237316195423570985008687907853269984665640564039457584007908834671663  )
	if ec.a == 0:
		print("y^2 = " + "x^3 + " + str(ec.b))	
	elif ec.a != 1:
		print("y^2 = " + "x^3 + " + str(ec.a)+"x + " + str(ec.b))
	else:
		print("y^2 = " + "x^3 + " + "x + " + str(ec.b))


	#calculate the order of E in GP/PARI
	numberPoints = subprocess.run('echo ellcard(ellinit([0,7]),115792089237316195423570985008687907853269984665640564039457584007908834671663) | gp -q', stdout=subprocess.PIPE, text=True, shell=True) 
	print("The order of E is: ", numberPoints.stdout)
	n = subprocess.run('echo ellorder(ellinit([0,7],115792089237316195423570985008687907853269984665640564039457584007908834671663),[55066263022277343669578718895168534326250603453777594175500187360389116729240, 32670510020758816978083085130507043184471273380659243275938904335757337482424]) | gp -q', stdout=subprocess.PIPE, text=True, shell=True)
	N = int(n.stdout)
	print("-"*80)


	print("The point we're using is:")
	P = (int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798",16),int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8",16))
	print(P)
	print("The order of this point is:")
	print(N)
	#run isprime in GP/PARI
	nprime = subprocess.run('echo isprime(ellorder(ellinit([0,7],115792089237316195423570985008687907853269984665640564039457584007908834671663),[55066263022277343669578718895168534326250603453777594175500187360389116729240, 32670510020758816978083085130507043184471273380659243275938904335757337482424])) | gp -q', stdout=subprocess.PIPE, text=True, shell=True)
	print("The order of the point is prime?")
	print(bool(nprime))


	b = random.randrange(1,N)
	a = random.randrange(1,N)
	bP = ec.multiply(b,P)
	aP = ec.multiply(a,P)
	abP = ec.multiply(a*b,P)


	print("Alice's private key is: ", a)
	print("Alice's public key is: ", aP)
	print("Bob's private key is: ",b)
	print("Bob's public key is: ", bP)
	print("The exchanged value is: ", abP)


	message_in = print("Alice, enter your message to be encrypted: \n")
	message_in = '\n'.join(iter(input, ""))
	print("The encrypted message is:")
	encrypted = encrypt(message_in,abP)
	encrypted_str = ' '.join(str(e) for e in encrypted)
	print(encrypted_str)
	print("The decrypted message is:")
	print(decrypt(encrypted,abP	))
