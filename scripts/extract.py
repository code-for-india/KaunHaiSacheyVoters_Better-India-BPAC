import json, sys
reload(sys)
sys.setdefaultencoding('utf-8')
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def emit(cont):
	result = []
	for k in content:
		result.append(k+":"+content[k])
	print "|||".join(str(x) for x in result)

#fh = open('English.txt')
fh = open('Marathi5.txt')
fl = 0;
avail = 0
output = []
feature_list = set()
for text in fh:
	text = text.strip()
	#print text
	if(text == "Page 3"):
		fl = 1
		content = {}
	if(fl == 1):
		content = {}
		# if(text == "Available"):
		# 	avail=1
		# 	continue
		# if(avail == 1 and is_number(text) == False):
		# 	break;
		if(is_number(text)):
			#print text
			feature_list.add('s_no')
			content['s_no'] = text
			avail = 0
			fl = 2
			continue
	if(fl == 2):
		feature_list.add('voter_id')
		content['voter_id'] = text
		fl = 3
		continue
	if(fl == 3):
		feature = text
		feature_list.add(feature)
		fl = 4
		continue
	if(fl == 4):
		if(text == "House number"):
			fl = 5
		else:
			content[feature] = text
			fl = 5
			continue
	if(fl == 5):
		feature_list.add(feature)
		feature = text
		fl = 6
		continue
	if(fl == 6):
		if(text.find("Age")!=-1):
			fl = 7
		else:
			content[feature] = text
			#print "asd",text
			fl = 7
			continue
	if(fl == 7):
		items = text.split(":")
		feature = items[0].strip()
		feature_list.add(feature)
		#print text
		val = items[1].strip()
		content[feature] = val
		fl = 8
		continue
	if(fl == 8):
		items = text.split(":")
		feature_list.add(feature)
		feature = items[0].strip()
		val = items[1].strip()
		content[feature] = val
		fl = 9
		continue
	if(fl == 9):
		feature_list.add('full_name')
		content['full_name'] = text
		fl = 10
		continue
	if(fl == 10):
		feature_list.add('photo')
		if(text.find("Photo") != -1):

			if(text.find("Not") != -1):
				content['photo'] = '0';
				fl = 1
				#print content
				emit(content)
				#output.append(content)
			else:
				content['photo'] = '1';
				fl = 1
				emit(content)
				#output.append(content)
				#print feature_list
				#print content
		else:
			continue

