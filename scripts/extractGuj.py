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
	content['photo'] = '0'
	for k in content:
		result.append(k+":"+content[k])

	print "|||".join(str(x) for x in result)

fh = open('Gujarathi5.txt')
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
		#content = {}
		if(text.find(":")!= -1):
			items = text.split(":")
			
			feature = items[0].strip()
			val = items[1].strip()
			if(feature == "Sex"):
				content["Gender"] = val
				emit(content)
				content = {}
				continue
			if(feature == "Category"):
				emit(content)
				content = {}
				continue
			feature_list.add(feature)
			content[feature] = val
			#print feature, val
		else:
			if(len(text)>4):
				content['voter_id'] = text
			else:
				content['s_no'] = text
