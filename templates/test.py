number_list = []

def calculate(x):
	i = 0
	while (i < x):
		number_list.append(i*10)
		i = i + 1
	print number_list

calculate(11)