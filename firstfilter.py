import json

input_file=open('rawdata.json', 'r')
rawdata_decode=json.load(input_file)
lst=[]

output_file=open('rawdata_filtered.json', 'w')


whitelist = open("whitelist.json", "r")
whitelist_decode=json.load(whitelist)
#whitelist_stack = whitelist_decode.split()

#print whitelist_stack

for i in rawdata_decode:
	print i
	for x in whitelist_decode:
		if(i['senderid']==x['senderid']):
			lst.append(i)


json.dump(lst,output_file,indent=4)
input_file.close()
output_file.close()
whitelist.close()