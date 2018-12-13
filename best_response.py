import numpy as np
import csv
def best_response(marginals_G_A, n_A_soldiers, n_B_soldiers, num_castles):
	values = [i+1 for i in range(num_castles)]
	# print("marginals_G_A",marginals_G_A[:5,:])
	Pi = np.zeros((n_B_soldiers+1, num_castles+1)) + np.nan
	H = np.zeros((n_B_soldiers +1, num_castles)) + np.nan
	ret_XB = [np.nan for i in range(num_castles)]
	
	for j in range(n_B_soldiers + 1):
		Pi[j,0] = 0
		for i in range(num_castles):
			# print("i,j", i,j)
			if j>n_A_soldiers:
				H[j, i] = values[i]
			else:
				H[j, i] = values[i] * (marginals_G_A[i, j-1] if j>0 else 0 )
			Pi[j,i+1] = max([Pi[k, i]+H[j-k, i] for k in range(j)] +[0])

	with open(r'temp.csv','w') as f:
	    writer = csv.writer(f)
	    writer.writerow("H")
	    for i in range(num_castles):
	    	writer.writerow(H[:,i])

	j = n_B_soldiers
	# print("Pi[:,num_castles-1]", Pi[:,num_castles-1])
	for i in range(num_castles-1,-1, -1):
		# https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
		# Only the first occurrence is returned
		# print("Pi[j-k, i-1 ]", Pi[j-k, i-1 ])
		# print("H[k,i]", H[k,i])
		# print("castle",i,"total",j, [Pi[j-k, i ] + H[k,i] for k in range(j)])

		ret_XB[i] = np.argmax([Pi[j-k, i ] + H[k,i] for k in range(j+1)]) 
		j = j - int(ret_XB[i])
	with open(r'temp.csv','a') as f:
	    writer = csv.writer(f)
	    writer.writerow("Pi")
	    for i in range(num_castles):
	    	writer.writerow(Pi[:,i])
	return ret_XB
