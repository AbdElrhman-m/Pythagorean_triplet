# superbido @bAbdElrhman-m

def Pythagorean_triplet (sum_n):
	""" 
	input: sum of 3 numbers as (a,b,c)
	process:  a < b < c
		a*a+b*b = c*c
		a + b + c = 1000
		c** 2 = a**2 +b**2
	output: a*b*c
	"""
	for a in range(1,sum_n+1):
		for b in range(1,sum_n+1):
			if a < b:
				if a + b + (a**2 + b **2)**0.5 == sum_n:
					c = (a**2+b**2)**0.5
					print "a: " + str(a) +' b: '+str(b) + " c: " + str(c) 	
					prod_ans = a * b * c		
					return "abc = "+ str(prod_ans)
## test code
print Pythagorean_triplet(12)
#>>> 60.0
print Pythagorean_triplet(1000)
#>>> 31875000.0
