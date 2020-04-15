import sys

class Rand(object):

	def __init__(self):
		self.seed = 0
		self.Xi = None

	def srand48(self,seedval=None):
		if seedval != None:		
			self.seed = seedval
		self.seed = (self.seed << 16) + 0x330E
	def drand48(self):
		if self.Xi == None:
			self.Xi = self.seed
		self.Xi = (0x5DEECE66D * self.Xi + 0xB ) & ( ( 1<<48 ) - 1 )
		return float(self.Xi) / (1 << 48)

def main():
	
	x = int( sys.argv[1] )
	rand48 = Rand()
	rand48.srand48(x)
	for val in range (10):

		next = rand48.drand48()
		print("results from drand48(): {} ".format(next))



if __name__ == '__main__':
	main()
