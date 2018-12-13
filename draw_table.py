import csv, sys
import numpy as np
import pandas as pd 

if __name__ == "__main__":
	num_of_interest = int(sys.argv[1])
	filename_output = "output_table_"+str(num_of_interest)+".csv"
	rows = []
	titles = []
	with open ("document.csv",'r') as f:
		csvReader= csv.reader(f)
		next(csvReader)
		next(csvReader)
		for row in csvReader:
			if num_of_interest == int(row[3]):
				rows.append(row)
				titles.append(row[0])
	print("titles", titles)
	Lists = []
	for row in rows:
		List = [int(row[j]) for j in range(4,len(row))]
		Lists.append(List)

	Mat = np.zeros((len(rows), len(rows)), dtype = np.int64) + np.nan
	for idx1, l1 in enumerate(Lists):
		for idx2, l2 in enumerate(Lists):
			Mat[idx1, idx2] = sum([(k+1)*int(l1[k] > l2[k])  for k in range(len(l1))])

	Mat = Mat.astype(int)
	Mat = Mat.astype(str)
	for idx1, l1 in enumerate(Lists):
		for idx2, l2 in enumerate(Lists):
			try:
				if int(Mat[idx1, idx2]) > int(Mat[idx2, idx1]):
					Mat[idx1, idx2] += '(win)'
				elif int(Mat[idx1, idx2]) < int(Mat[idx2, idx1]):
					Mat[idx2, idx1] += '(win)'
			except:
				pass
	 
	#-------
	# np.savetxt(filename_output,Mat)
	#-------
	print("Mat", Mat)
	print("Mat.shape", Mat.shape)
	df = pd.DataFrame(Mat)
	df.columns = titles
	df['mine/rival'] =titles
	df= df.set_index('mine/rival')
	df.to_csv(filename_output)


