from math import sqrt

def sum_of_divisors(n):
	sum_divisors = 0
	divisors = get_divisors(n)

	for num in divisors:
		sum_divisors += num

	return sum_divisors

def get_divisors(n):
	divisors = []

	current_divisor = 1
	last_divisor = n // 2

	while current_divisor <= last_divisor:
		if n % current_divisor == 0:
			divisors += [current_divisor]
		current_divisor += 1

	divisors += [n]

	return divisors

print (sum_of_divisors(8))
print (sum_of_divisors(7))
print (sum_of_divisors(1))
print (sum_of_divisors(1000))

print (10 * '-')

def is_prime(n):
	n = abs(n)
	is_n_prime = True

	if n == 1:
		return False

	first = 2

	while first < n:
		if n % first == 0:
			is_n_prime = False
		first += 1

	return is_n_prime

print (is_prime(1))
print (is_prime(2))
print (is_prime(8))
print (is_prime(11))
print (is_prime(-10))

print (10 * '-')

def contains_digit(number, digit):
	digits = []

	while number != 0:
		digits += [number % 10]
		number = number // 10

	if digit in digits:
		return True
	else:
		return False

print (contains_digit(123, 4))
print (contains_digit(42, 2))
print (contains_digit(1000, 0))
print (contains_digit(12346789, 5))

print (10 * '-')

def contains_digits(number, digits):
	are_digits_here = True
	number_digits = []

	while number != 0:
		number_digits += [number % 10]
		number = number // 10

	for digit in digits:
		if digit not in number_digits:
			return False

	return True

print (contains_digits(402123, [0, 3, 4]))
print (contains_digits(666, [6,4]))
print (contains_digits(123456789, [1,2,3,0]))
print (contains_digits(456, []))

print (10 * '-')

def is_number_balanced(n):
	digits = []

	while n != 0:
		digits += [n % 10]
		n = n // 10

	middle_index = int(len(digits) / 2)

	sum_left = 0
	sum_right = 0

	if len(digits) % 2 == 0:
		for i in range(0, middle_index):
			sum_left += digits[i]
		for i in range(middle_index, len(digits)):
			sum_right += digits[i]
	else:
		for i in range(0, middle_index):
			sum_left += digits[i]
		for i in range(middle_index + 1, len(digits)):
			sum_right += digits[i]

	if sum_left == sum_right:
		return True
	else:
		return False

print (is_number_balanced(9))
print (is_number_balanced(11))
print (is_number_balanced(13))
print (is_number_balanced(121))
print (is_number_balanced(4518))
print (is_number_balanced(28471))
print (is_number_balanced(1238033))

print (10 * '-')

def count_substrings(haystack, needle):

	counter = haystack.count(needle, 0, len(haystack))

	return counter

print (count_substrings("This is a test string", "is"))
print (count_substrings("babababa", "baba"))
print (count_substrings("Python is an awesome language to program in!", "o"))
print (count_substrings("We have nothing in common!", "really?"))
print (count_substrings("This is this and that is this", "this"))

print (10 * '-')

def zero_insert(n):
	n_list = []
	result = []

	n_list = [int(x) for x in str(n)]
	
	last_digit = n_list[len(n_list) - 1]

	for i in range(0, len(n_list) - 1):
		result.append(n_list[i])

		digit = n_list[i + 1]

		if n_list[i] == n_list[i + 1] or (n_list[i] + n_list[i + 1]) % 10 == 0:
			result.append(0)

		#result.append(digit)

	result.append(last_digit)

	print (result)

	#result = [str(x) for x in result]
	#print (result)

	#str_result = "".join(result)

	#bum = int(str_result)

	number = 0

	for digit in result:
		number = number * 10 + digit

	return number

print (zero_insert(116457))
print (zero_insert(55555555))
print (zero_insert(1))
print (zero_insert(6446))

print (10 * '-')

def sum_matrix(m):
	result = 0

	for i in range (0, len(m)):
		for j in range(0, len(m[i])):
			result += m[i][j]

	return result

print (sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print (sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print (sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

print (10 * '-')

import copy

def matrix_bombing_plan(m):
	
	result = {}
	#result[(0, 0)] = 5
	
	copied_m = copy.deepcopy(m)

	for i in range(0, len(m)):
		
		for j in range(0, len(m[i])):

			m = copy.deepcopy(copied_m)

			element = m[i][j]
			#sum_elements = 0
			#result[(i, j)] = 0



			if i + 1 < len(m):
				if m[i + 1][j] - m[i][j] >= 0:
					m[i + 1][j] = m[i + 1][j] - m[i][j]
				else:
					m[i + 1][j] = 0

			if i - 1 >= 0:
				if m[i - 1][j] - m[i][j] >= 0:
					m[i - 1][j] = m[i - 1][j] - m[i][j]
				else:
					m[i - 1][j] = 0

			if j + 1 < len(m[i]):
				if m[i][j + 1] - m[i][j] >= 0:
					m[i][j + 1] = m[i][j + 1] - m[i][j]
				else:
					m[i][j + 1] = 0

			if j - 1 >= 0:
				if m[i][j - 1] - m[i][j] >= 0:
					m[i][j - 1] = m[i][j - 1] - m[i][j]
				else:
					m[i][j - 1] = 0

			if i + 1 < len(m) and j + 1 < len(m[i]):
				if m[i + 1][j + 1] - m[i][j] >= 0:
					m[i + 1][j + 1] = m[i + 1][j + 1] - m[i][j]
				else:
					m[i + 1][j + 1] = 0

			if i + 1 < len(m) and j - 1 >= 0:
				if m[i + 1][j - 1] - m[i][j] >= 0:
					m[i + 1][j - 1] = m[i + 1][j - 1] - m[i][j]
				else:
					m[i + 1][j - 1] = 0

			if i - 1 >= 0 and j + 1 < len(m[i]):
				if m[i - 1][j + 1] - m[i][j] >= 0:
					m[i - 1][j + 1] = m[i - 1][j + 1] - m[i][j]
				else:
					m[i - 1][j + 1] = 0

			if i - 1 >= 0 and j - 1 >= 0:
				if m[i - 1][j - 1] - m[i][j] >= 0:
					m[i - 1][j - 1] = m[i - 1][j - 1] - m[i][j]
				else:
					m[i - 1][j - 1] = 0

			sum_elements = 0

			print (m)

			for k in range (0, len(m)):
				for p in range(0, len(m[k])):
					sum_elements += m[k][p]

			result[(i, j)] = sum_elements


					

	print (result)

matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])