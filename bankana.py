#msg template keywords
#classifier
#giving points to particular banks based on nuber of keyboards and temlpates satisfied 
import re
#############################################################################################
########################[SMS ANALYSER _ ACCOUT BALANCE ONLY]#################################
#############################################################################################

##############################[KNOWLEDGE_BASE]###############################################

def check_fgb( input_clean, no_of_x, no_of_accno ):
	
	fgb_template1 = ["dear", "customer", "available", "balance", "ac", "aed"]
	fgb_template1_no_of_x = 8.0000
	fgb_template1_no_of_accno = 6.0000
	fgb_template1_date = len(re.findall(r'\d{2}-\d{2}-\d{4}',input_clean))
	fgb_template1_time = len(re.findall(r'\d{2}:\d{2}:\d{2}',input_clean))
	fgb_template1_amount = len(re.findall(r'(\d+)\.[0-9]{2}',input_clean))
	i = 0
	for x in fgb_template1:
	     if(x in input_clean.lower()):
	          i+=1

	fgb_template2 = [ "balance", "a/c", "eod", "aed", "check", "current", "credits", "subject", "clearing"]
#	fgb_template2 = [ "balance", "a/c", "eod", "aed", "check", "current", "balance", "credits", "a/c", "subject", "clearing"]
	fgb_template2_no_of_x = 12.0000
	fgb_template2_no_of_accno = 4.0000
	fgb_template2_date = len(re.findall(r'\d{2}-\w{3}-\d{2}',input_clean))
	fgb_template2_amount = len(re.findall(r'(\d+)\,[0-9]{2}',input_clean))
	ii = 0
	for x in fgb_template2:
	     if(x in input_clean.lower()):
	          ii+=1

	fgb_template1_score = (i/len(fgb_template1) + no_of_x/fgb_template1_no_of_x + no_of_accno/fgb_template1_no_of_accno + fgb_template1_date + fgb_template1_time + fgb_template1_amount)/0.0600
	fgb_template2_score = (ii/len(fgb_template2) + no_of_x/fgb_template2_no_of_x + no_of_accno/fgb_template2_no_of_accno + fgb_template2_date + fgb_template2_amount)/0.0500
	print "score for fgb template 1:",fgb_template1_score," template 2:",fgb_template2_score


def check_hsbc( input_clean, no_of_accno ):
	
#	hsbc_template1 = [ "balance", "saving", "a/c", "eod", "aed", "eod", "credits", "a/c", "subject", "clearing", "know", "more", "use", "hsbc","mobile", "/hsbc.ae/mobile"]
	hsbc_template1 = [ "balance", "saving", "a/c", "eod", "aed", "eod", "credits", "subject", "clearing", "know", "more", "use", "hsbc","mobile", "/hsbc.ae/mobile"]
	hsbc_template1_no_of_accno = 6.0000
	hsbc_template1_date = len(re.findall(r'\d{2}-\w{3}-\d{4}',input_clean))
	hsbc_template1_amount = len(re.findall(r'(\d+)\.[0-9]{2}',input_clean))
	i = 0
	for x in hsbc_template1:
	     if(x in input_clean.lower()):
	          i+=1          

	hsbc_template1_score = (i/len(hsbc_template1) + no_of_accno/hsbc_template1_no_of_accno + hsbc_template1_date + hsbc_template1_amount)/0.0400
	print "score for hsbc template 1:",hsbc_template1_score

#know and check are diff
#balance added incase nonbank statement added
#TODO
#export out the numerical value and check decimals
#export ac number as coming after ac .. then check for charecters in it

######################################################################################################


common_words = ['as','on','to','your','for', 'are' , 'of' ]

#positive_phrases = [ 'available balance', 'balance in' ]

#negative_phrases = [ 'loan balance', 'loan account balance', 'debt', 'fine' ]


input_raw = "Balance in a/c XXXXXXXXXXXX1234 as of 22-FEB-16 EOD is AED 10000,00 . Check a/c for current balance. Credits in a/c are subject to clearing."
input_strip = input_raw.split(' ')

resultwords  = [word for word in input_strip if word.lower() not in common_words]
input_clean = ' '.join(resultwords)

no_of_x=len(re.findall(r'[xX]',input_clean))
accno=re.findall(r'[xX]*([0-9]+)',input_clean)
no_of_accno = len(accno[0])


check_fgb(input_clean, no_of_x, no_of_accno)
check_hsbc(input_clean, no_of_accno)



