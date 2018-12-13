import numpy as np
# DIU_strategy
import random

def r_func(m,x):
	ret = np.floor(m*x+0.5)*1.0/m
	return ret 

def DIU(n_A_soldiers, n_B_soldiers, num_castles):
	values = [i +1 for i in range(num_castles)]
	flag_switch = n_A_soldiers > n_B_soldiers
	if flag_switch:
		temp = n_B_soldiers
		n_B_soldiers = n_A_soldiers
		n_A_soldiers = temp
		del temp
	# input n_A_soldiers, n_B_soldiers, num_castles, values
	# output: hat X A, hat X B
	ret_xA = np.zeros(num_castles, dtype = int) + np.nan
	ret_xB = np.zeros(num_castles, dtype = int) + np.nan

	Vn = sum(values)
	Lambda = n_B_soldiers *1.0/ n_A_soldiers
	a = np.zeros((1,num_castles))
	while 0 == np.sum(a):
		# print(np.sum(a))
		a = np.random.binomial(n = 1, p = 1.0/Lambda, size = num_castles) \
		* np.array([2*values[i]*Lambda/ Vn - np.random.uniform(low = 0,high = 2*values[i]*Lambda/ Vn) for i in range(num_castles)])

	b = np.array([2*values[i]*Lambda/ Vn - np.random.uniform(low = 0,high = 2*values[i]*Lambda/ Vn) for i in range(num_castles)])

	SA = np.zeros(num_castles + 1) + np.nan
	SA[0] = 0
	SB = np.zeros(num_castles + 1) + np.nan
	SB[0] = 0
	sum_a = np.sum(a)
	sum_b = np.sum(b)
	# print("a",a)
	# print("b",b)
	for i in range(num_castles):
		SA[i+1] = np.sum(a[:i])/sum_a
		SB[i+1] = np.sum(b[:i])/sum_b *Lambda
		ret_xA[i] = np.floor(n_A_soldiers*SA[i+1]+0.5) - np.floor(n_A_soldiers*SA[i]+0.5)
		ret_xB[i] = np.floor(n_A_soldiers*SB[i+1]+0.5) - np.floor(n_A_soldiers*SB[i]+0.5)
	# print("ret_xA", ret_xA)
	ret_xA = ret_xA.astype(int)
	# print("ret_xA.astype(int)", ret_xA)
	ret_xB = ret_xB.astype(int)
	if flag_switch:
		temp = ret_xB
		ret_xB = ret_xA
		ret_xA = temp
		del temp
	return ret_xA, ret_xB

