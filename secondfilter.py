import json
import re


def getaccno(pos, msgstring):
	msgstring = msgstring.split(' ')
	temp = msgstring[pos].strip('X')
	return temp

def getbal(pos, msgstring):
	msgstring = msgstring.split(' ')
	temp = msgstring[pos]
	return temp

def getdate(pos, msgstring):
	msgstring = msgstring.split(' ')
	temp = msgstring[pos]
	return temp

def scoremsg(patten, content):
	#direct matching with re templ
	temp = len(re.findall(pat, j['content']))*100
	return temp
	#TODO scoring mecansim
	#keywords


	

input_file=open('rawdata_filtered.json', 'r')
rawdata_decode=json.load(input_file)


#lst=[[0 for i in range(4)] for i in range(len(rawdata_decode))] #0 for i in range(4)
lst=[]
output_file=open('account_info.json', 'w')

templates = open("templates.json", "r")
templates_decode=json.load(templates)


#TODO referencing same accno
flag=0
for i in templates_decode:
	for j in rawdata_decode:

		pat= re.compile(i['regex'])
		if (scoremsg(pat, j['content']) >= 95):
			accno = getaccno(i['posaccno'],j['content'])
			bal = getbal(i['posbalno'],j['content'])
			date = getbal(i['posdate'],j['content'])

			#rule out the cases where msgs from same bank and same accno
			if len(lst)==0:
				print "prin only once"
				lst.append([i['Bank Name'], i['country'], accno,bal,date])
			else:
				for z in range (len(lst)):
					if (accno==lst[z][2] and i['Bank Name']==lst[z][0]):
						print "pusi found"
						flag=1
						break
					else:
						flag=0
				if flag==0:
					lst.append([i['Bank Name'], i['country'], accno,bal,date])
				elif flag==1:
				 	print "same pussi"
				 	lst[z][3]=bal
				 	lst[z][4]=date




json.dump(lst,output_file,indent=4)
input_file.close()
output_file.close()
templates.close()
print "End of all loop gods"

