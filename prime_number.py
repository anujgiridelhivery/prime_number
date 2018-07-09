# check prime numbers in given list

# num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def prime(data):
	prime_list = []
	for num in data:
		for item in range(2,num):
			if num%item == 0:
				break
		else:
			prime_list.append(num)
	return prime_list
