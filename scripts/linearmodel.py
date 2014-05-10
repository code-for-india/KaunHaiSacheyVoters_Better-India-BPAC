from sklearn.linear_model import LinearRegression as lr
import json, math
import numpy as np
def gen_train():
 	fake_list=[39, 45, 83, 171, 180, 181, 185, 187, 190, 194, 195, 212, 297, 338, 342, 344, 404, 415, 428, 509, 514, 515, 516, 517, 559, 635, 637, 752, 755, 770, 802, 907, 908, 913, 922, 932, 942, 943, 1038, 1056] 
	fh = open('data_scores.json')
	contents = json.load(fh)
	print contents
	for x in contents:
		if(int(x['s_no']) in fake_list):
			print x
			print "\n\n"

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def trainModel():
	fh = open('train.features')
	X = []
	for x in fh:
		x = x.strip()
		x = x.split(',')
		x = [int(x1) for x1 in x]

		X.append(x)
	fh.close()
	fh = open('train.labels')
	Y = []
	for y in fh:
		y = y.strip()
		Y.append(int(y))
	fh.close()
	clf = lr()
	clf.fit(X,Y)
	print sigmoid(clf.predict(X[45]))
	print clf.coef_
	#np.save("lr_coeff",clf.coef_)
	print clf.intercept_
	#np.save("lr_intercept",clf.intercept_)
	score = np.dot(clf.coef_, X[45])+ clf.intercept_
	print sigmoid(score)

	coeff = np.load("lr_coeff.npy")
	intercept = np.load("lr_intercept.npy")
	score = np.dot(coeff, X[45]) + intercept
	print sigmoid(score)	

trainModel()