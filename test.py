from DIU import DIU
from best_response import best_response
import time, csv   
import numpy as np
import multiprocessing

import sys


def para_func(iter):
	xA,xB = DIU(n_A_soldiers, n_B_soldiers, num_castles = n_castles) # xAs.append(xA)
	if 0 == (iter+1)%iter_print:
		print("iter",iter, "elapsed time", time.time() - T0)
		# xBs.append(xB)
	return xA
if __name__ == "__main__":

	n_castles = int(sys.argv[1])
	n_A_soldiers = int(sys.argv[2])
	n_B_soldiers = int(sys.argv[3])
	
	n_simulations = 400000 # 2^{100}
	iter_print = n_simulations/10#100000
	T0 = time.time()
	#------
	num_of_cores = multiprocessing.cpu_count()
	print("num_of_cores", num_of_cores)
	pool = multiprocessing.Pool(processes=num_of_cores)
	xAs = [pool.apply(para_func, args=(iter,)) for iter in range(n_simulations)]
	#---------
	# xAs = []
	# for iter in range(n_simulations):
	# 	xA = para_func(iter)
	# 	xAs.append(xA)

	marginals_G_A = np.zeros((n_castles, n_A_soldiers+1)) 
	for xA in xAs:
		for n_cast in range(n_castles):
			marginals_G_A[n_cast, xA[n_cast]] = marginals_G_A[n_cast, xA[n_cast]]+ 1
	marginals_G_A = (marginals_G_A.T/ marginals_G_A.sum(axis = 1)).T
	# print("--------")
	# print("marginals_G_A",marginals_G_A[:3,:])
	marginals_G_A = np.cumsum(marginals_G_A, axis = 1)
	# print("marginals_G_A",marginals_G_A[:3,:])
	# print("--------")
	best_B = best_response(marginals_G_A, n_A_soldiers, n_B_soldiers, num_castles = n_castles)
	with open(r'document.csv', 'a') as f:
	    writer = csv.writer(f)
	    writer.writerow([n_simulations,n_castles, n_A_soldiers,n_B_soldiers]+best_B)
