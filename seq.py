def sequences():

	sequences = []

	# Rows

	sequences.append([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
	sequences.append([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)])
	sequences.append([(0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])

	sequences.append([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)])
	sequences.append([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)])
	sequences.append([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)])

	sequences.append([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
	sequences.append([(2, 1), (2, 2), (2, 3), (2, 4), (2, 5)])
	sequences.append([(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)])

	sequences.append([(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)])
	sequences.append([(3, 1), (3, 2), (3, 3), (3, 4), (3, 5)])
	sequences.append([(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])

	sequences.append([(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])
	sequences.append([(4, 1), (4, 2), (4, 3), (4, 4), (4, 5)])
	sequences.append([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)])

	sequences.append([(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)])
	sequences.append([(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)])
	sequences.append([(5, 2), (5, 3), (5, 4), (5, 5), (5, 6)])

	sequences.append([(6, 0), (6, 1), (6, 2), (6, 3), (6, 4)])
	sequences.append([(6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
	sequences.append([(6, 2), (6, 3), (6, 4), (6, 5), (6, 6)])

	# Columns

	sequences.append([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
	sequences.append([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
	sequences.append([(2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])

	sequences.append([(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)])
	sequences.append([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)])
	sequences.append([(2, 1), (3, 1), (4, 1), (5, 1), (6, 1)])

	sequences.append([(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)])
	sequences.append([(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)])
	sequences.append([(2, 2), (3, 2), (4, 2), (5, 2), (6, 2)])

	sequences.append([(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)])
	sequences.append([(1, 3), (2, 3), (3, 3), (4, 3), (5, 3)])
	sequences.append([(2, 3), (3, 3), (4, 3), (5, 3), (6, 3)])

	sequences.append([(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)])
	sequences.append([(1, 4), (2, 4), (3, 4), (4, 4), (5, 4)])
	sequences.append([(2, 4), (3, 4), (4, 4), (5, 4), (6, 4)])

	sequences.append([(0, 5), (1, 5), (2, 5), (3, 5), (4, 5)])
	sequences.append([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
	sequences.append([(2, 5), (3, 5), (4, 5), (5, 5), (6, 5)])

	sequences.append([(0, 6), (1, 6), (2, 6), (3, 6), (4, 6)])
	sequences.append([(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)])
	sequences.append([(2, 6), (3, 6), (4, 6), (5, 6), (6, 6)])

	# Diagonals

	sequences.append([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
	sequences.append([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
	sequences.append([(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])

	sequences.append([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])
	sequences.append([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])
	
	sequences.append([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)])

	sequences.append([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)])
	sequences.append([(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)])
	
	sequences.append([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4)])

	sequences.append([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2)])
	sequences.append([(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)])
	sequences.append([(2, 4), (3, 3), (4, 2), (5, 1), (6, 0)])

	sequences.append([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1)])
	sequences.append([(1, 4), (2, 3), (3, 2), (4, 1), (5, 0)])
	
	sequences.append([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)])

	sequences.append([(1, 6), (2, 5), (3, 4), (4, 3), (5, 2)])
	sequences.append([(2, 5), (3, 4), (4, 3), (5, 2), (6, 1)])
	
	sequences.append([(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)])

	return sequences
	

