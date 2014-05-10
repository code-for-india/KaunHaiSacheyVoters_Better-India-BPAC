# -*- coding: utf-8 -*-
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import codecs, sys
reload(sys)
sys.setdefaultencoding('utf-8')

def translate(to_translate, to_langage="auto", langage="hi"):
	'''Return the translation using google translate
	you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?'''
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    cnt = 0
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        # print cnt
        # print len(retstr.getvalue())
        # cnt+=1
    fp.close()
    device.close()

    str = retstr.getvalue()
    print len(str.split("\n"))
    retstr.close()
    return str

# text =  convert_pdf_to_txt('hindi.pdf')
# out = codecs.open('eng.txt',"w+", 'utf-8')
# words = text.split(" ")
# out.write(text)

# to_translate = 'Hola como estas?'
# to_translate = words[0]+" "+words[1]
# to_translate = 'ગઢવી ઉદયદાન'
# for word in words:
#     print("%s >> %s" % ("translate", translate(word)))

#print("%s >> %s" % (to_translate, translate(to_translate, 'en')))
	#should print Hola como estas >> Hello how are you
	#and Hola como estas? >> Bonjour comment allez-vous?

fh = codecs.open('eng.txt', encoding='utf-8')
out = codecs.open("english.txt", "w+", "utf-8")
for text in fh:
    words = text.split(" ")
    for word in words:
        #print("%s >> %s" % ("translate", translate(text)))
         out.write(translate(word)+"\n")