#test_julia_output.py
import numpy as np
from best_response import best_response
import sys, csv 

if __name__ == "__main__":
	filename = "ColonelBlotto/distri_90_100a.csv"
	list_split = filename.split('_')
	n_castles = 10
	n_B_soldiers = int(list_split[1])
	n_A_soldiers = int(list_split[2].split('.')[0][:-1])

	del list_split

	marginals_G_A = np.genfromtxt(filename, delimiter=',')
	# print("--------")
	# print("marginals_G_A",marginals_G_A[:3,:])
	marginals_G_A = np.cumsum(marginals_G_A, axis = 1)
	# print("marginals_G_A",marginals_G_A[:3,:])
	# print("--------")
	best_B = best_response(marginals_G_A, n_A_soldiers, n_B_soldiers, num_castles = n_castles)
	with open(r'document.csv', 'a') as f:
	    writer = csv.writer(f)
	    writer.writerow(["Julia", n_castles, n_A_soldiers,n_B_soldiers] + best_B)