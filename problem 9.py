# superbido 
# >>>  https://github.com/superbido


# a<b<c
#a*a+b*b = c*c
# a + b + c = 1000
# c** 2 = a**2 +b**2


def Pythagorean_triplet (sum_n):
	for a in range(1,sum_n+1):
		for b in range(1,sum_n+1):
			if a < b:
				if a + b + (a**2 + b **2)**0.5 == sum_n:
					c = (a**2+b**2)**0.5
					print "a: " + str(a) +' b: '+str(b) + " c: " + str(c) 	
					prod_ans = a * b * c		
					return "abc = "+ str(prod_ans)

print Pythagorean_triplet(12)
print Pythagorean_triplet(1000)