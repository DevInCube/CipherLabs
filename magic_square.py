# http://blog.dreamshire.com/panmagic-pandiagonal-magic-square-generation-testing/
# https://ru.wikipedia.org/wiki/????????????_?????????????#

import string

def make_magic_square(n):
	if n < 1 or n == 2:
		return False
	if n % 2 == 1:
		return make_odd_magic_square(n)
	else:
		if n % 4 == 0:
			return make_even_4n_magic_square(n)
		elif (n-2) % 4 == 0:
			return make_even_4np2_magic_square(n)
		else:
			return False

def make_odd_magic_square(n):

	if n < 1 or n%2 == 0: return False	#only allow odd squares 2n-1, n>0

	J = [range(1, n+1)] * n
	I = transpose(J)

	A = [[(I[i][j] + J[i][j] + (n-3)/2) % n for i in range(n)] for j in range(n)]
	B = [[(I[i][j] + 2*J[i][j] - 2) % n for j in range(n)] for i in range(n)]

	return [[n*A[i][j] + B[i][j] + 1 for j in range(n)] for i in range(n)]


def make_even_4np2_magic_square(n):

	nx, k = n/2, (n-2)/4
	if n < 6 or nx % 2 == 0: return False	#only allow even squares 4n+2, n>1

	#make an odd nx x nx magic square
	A = make_odd_magic_square(nx)

	#fill in each quadrant with an augmentation of A according to algorithm
	I = A + sc_add(A, 3*nx*nx)
	J = sc_add(A, 2*nx*nx) + sc_add(A, nx*nx)

	#create initial square by concatenating I and J - column sums are "magic"
	B = [I[i]+J[i] for i in range(n)]

	#swap upper and lower halves of specific columns to make row sums "magic"
	for j in range(k) + range(n-1, n-k, -1):
		for i in range(nx):
			B[i][j], B[i+nx][j] =  B[i+nx][j], B[i][j]

	#switch middle values for 2 columns to make diagonals (and square) magic
	B[nx-k-1][k-1], B[nx+k][k-1] = B[nx+k][k-1], B[nx-k-1][k-1]
	B[nx-k-1][k], B[nx+k][k] = B[nx+k][k], B[nx-k-1][k]

	return B


def make_even_4n_magic_square(n):

	if n < 4 or n%4: return False	#only allow even squares 4n, n>0

	c, cms, A = 1, n*n + 1, [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			A[i][j] = cms-c if i%4 == j%4 or (i+j)%4 == (n-1)%4 else c
			c += 1

	return A

def transpose(A):
	return [list(a) for a in zip(*A)]

def sc_add(A, n):
	"""
	Scalar add n to matrix A
	"""
	return [[x+n for x in row] for row in A]

def print_matrix(matrix):
    print(*matrix, sep='\r\n')

if __name__ == "__main__":
    matrix = make_magic_square(5)
    print_matrix(matrix)
