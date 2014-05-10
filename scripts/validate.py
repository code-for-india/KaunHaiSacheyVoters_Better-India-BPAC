import re, random, math
import numpy as np
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def validate_voter_id(s):
	if(re.search(r"[A-Z]{3}[0-9]{7}", s)!= None):
		return 1
	return 0

def validate_names(relation_name, full_name):
	name1 = set(relation_name.split(' '))
	name2 = set(full_name.split(' '))
	common = name1.intersection(name2)
	if(common != ""):
		return 1
	return 0

def compute_age_dist(contents):
	bad_ages = []
	age_dist = {}
	cnt = 0
	for x in contents:
		if(x.has_key('Age')):
			if(is_number(x['Age'])):
				age = int(x['Age'])
				cnt+=1
				if(age_dist.has_key(str(age/10))):
					age_dist[str(age/10)] += 1
				else:
					age_dist[str(age/10)] = 1

	for x in age_dist:
		if(age_dist[x] >= cnt/3):
			bad_ages.append(x)
	#print age_dist
	#print bad_ages
	return bad_ages

def compute_name_dist(contents):
	name_dist = {}
	bad_names = []
	for x in contents:
		if(x.has_key('full_name')):
			name = x['full_name'].lower()
			if(name_dist.has_key(name)):
				name_dist[name] +=1
			else:
				name_dist[name] = 1
	for k in name_dist:
		if(name_dist[k] > 10 and len(k) > 4):
			bad_names.append(k)
	return bad_names
	#print name_dist

def map_names(contents):
	names = set()
	for x in contents:
		if(x.has_key('full_name')):
			names.add(x['full_name'])
	return names

def get_features(item, bad_names, bad_ages):
	NUM_FEATS = 9
	house_num_present = 0
	gender_present = 1
	age_valid_present = 2
	photo_present = 3
	voter_id_valid = 4
	relation_name_overlap_present = 5
	relation_name_present = 6
	relation_name_valid = 7
	duplicate_name_present = 8
	bad_age_present = 9
	features = [0]*NUM_FEATS
	#print item
	if(item.has_key('house_number')):
		features[house_num_present] = 1
	if(item.has_key('Gender')):
		features[gender_present] = 1
	if(item.has_key('Age') and is_number(item['Age'])):
		if(int(item['Age']) >= 18 and int(item['Age']) <= 100):
			features[age_valid_present] = 1
	if(item.has_key('photo')):
		features[photo_present] = 1
	if(item.has_key('voter_id')):
		if(validate_voter_id(item['voter_id']) == True):
			features[voter_id_valid] = 1
	if(item.has_key('father_name') or item.has_key('mother_name') or item.has_key('patice_name')):
			features[relation_name_present] = 1
			if(item.has_key('father_name')):
				relation_name = 'father_name'
			if(item.has_key('mother_name')):
				relation_name = 'mother_name'
			if(item.has_key('patice_name')):
				relation_name = 'patice_name'
			if(item.has_key('full_name') and validate_names(item[relation_name], item['full_name']) ==  True):
				features[relation_name_overlap_present] = 1

	#group features
	if(item.has_key('full_name')):
		if(item['full_name'] in bad_names):
			features[duplicate_name_present] = 1
	# if(item.has_key('Age')):
	# 	if(str(int(item['Age'])/10) in bad_ages):
	# 		features[bad_age_present] = 1

	return features




# for item in contents:
# 	get_features(item, bad_names, bad_ages)
# 	break
def gen_train(bad_names, bad_ages):
 	fake_list=[39, 45, 83, 171, 180, 181, 185, 187, 190, 194, 195, 212, 297, 338, 342, 344, 404, 415, 428, 509, 514, 515, 516, 517, 559, 635, 637, 752, 755, 770, 802, 907, 908, 913, 922, 932, 942, 943, 1038, 1056] 
	fh = open('data_scores.json')
	contents = json.load(fh)
	selected = []
	#print contents
	for x in range(450):
		num = 1 +random.randint(0,1000)
		if(num  not in fake_list):
			selected.append(num)
	for x in contents:
		num = random.randint(0,1000)
		if(int(x['s_no']) in selected):
			features = get_features(x, bad_names, bad_ages)
			print ",".join(str(x) for x in features)
			#print 1
	#print selected		
	fh.close()

import json
# fh = open('data_scores.json')
# contents = json.load(fh)
# bad_ages = compute_age_dist(contents)
# bad_names = compute_name_dist(contents)
# names = map_names(contents)
# gen_train(bad_names, bad_ages)


#fh = open('guj1.json')
fh = open('data_scores.json')
#fh = open('tempg.json')
contents = json.load(fh)
bad_ages = compute_age_dist(contents)
bad_names = compute_name_dist(contents)
names = map_names(contents)
coeff = np.load("lr_coeff.npy")
intercept = np.load("lr_intercept.npy")

for x in contents:
	features = get_features(x, bad_names, bad_ages)
	#print ",".join(str(x) for x in features)
	y =sigmoid(np.dot(coeff, features) + intercept)
	x['ind_score'] = y*10
	x['grp_score'] = 1+random.randint(0,9)
	x['voting_history'] = 0
	x['birth_validation'] = 0
	x['death_validation'] = 0

print json.dumps(contents)