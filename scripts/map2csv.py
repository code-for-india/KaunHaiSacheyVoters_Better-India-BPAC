import json, re
import sys
import random
from random import randrange
reload(sys)
sys.setdefaultencoding('utf-8')
fh = open('gparse2.txt')
feature_list = ['house_number', 'voter_id', 'Gender', 'photo', 's_no', 'full_name', 'Age', 'father_name', 'patice_name', 'mother_name', 'ind_score', 'grp_score', 'voting_history', 'birth_validation', 'death_validation']

#eature_list = ['house_number', 'voter_id', 'Gender','s_no', 'full_name', 'Age', 'father_name','patice_name', 'mother_name', 'ind_score', 'grp_score', 'voting_history', 'birth_validation', 'death_validation']
#eature_values = ['']*15
feature_values = {}
#rint ",".join(feature_list)
result =[]
for text in fh:
	text = text.strip()
	#text = re.sub(r"[}{']","", text)
	words = text.split("|||")
	#eature_values = ['']*15
	feature_values = {}
	for word in words:
		#print word
		if(word==""):
			continue
		key, value = word.split(":")
		#key = re.sub("'","" ,key)
	# 	pos = feature_list.index(key.strip())
	# 	feature_values[pos] = str(value.strip())
	# feature_values[9+1] =  str(1+random.randint(0,9))
	# feature_values[9+2] =  str(1+random.randint(0,9))
	# feature_values[9+3] = '0'
	# feature_values[9+4] = '0'
	# feature_values[9+5] = '0'
	# print ",".join(feature_values)
	
		feature_values[key] = value.strip()
	feature_values['ind_score'] = 1+random.randint(0,9)
	feature_values['grp_score'] = 1+random.randint(0,9)
	feature_values['voting_history'] = 0
	feature_values['birth_validation'] = 0
	feature_values['death_validation'] = 0

		#print feature_values['ind_score']
	result.append(feature_values)
#rint len(result)

print json.dumps(result)
