def print_matrix_integer(matrix=[[]]):
	for rows in matrix:
		for i in rows:
			if  rows.index(i)  != len(rows) - 1:
				print("{:d}".format(i), end=' ')
			else:
				print("{:d}".format(i))
	print('--')
	print()
if __name__ == "__main__":
	matrix = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	print_matrix_integer(matrix)
