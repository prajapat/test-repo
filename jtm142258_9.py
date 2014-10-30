#!/usr/bin/python

#initialization of variables
Happy = 0
Sad = 0
Sarcastic = 0
Surprised = 0
Crook = 0
Neutral = 0
Angry = 0

#opening and reading a file
with open('content.txt','r') as file:
	for line in file.readlines():

		#Calculation of A's Emoticons
		if line[0] == "A":
        		for words in line.split():#splitting the line word by word

				#counting emoticons
				if ( words == ':)' or words == ':D' ):
			    		Happy += 1
				elif ( words == ':(' or words == ":'(" ):
			    		Sad += 1
		       		elif ( words == ':P' or words == ';)' ):
			    		Sarcastic += 1
		       		elif ( words == ':-o' or words == 'O_O' ):
			  		Surprised += 1
				elif ( words == 'B-)' or words == ';)' ):
			    		Crook += 1
				elif ( words == ':-/' or words == '=_=' ):
			    		Neutral += 1
				elif ( words == 'x-(' or words == '>_<' ):
			    		Angry += 1
	print"A's Emoticons are:-"
    	print"Happy = ",Happy
   	print"Sad = ",Sad
	print"Sarcastic = ",Sarcastic
    	print"Surprised = ",Surprised
    	print"Crook = ",Crook
    	print"Neutral = ",Neutral
    	print"Angry = ",Angry
	print"\n"



	#Calculation of B's Emoticons
	if line[0] == "B":
        	for words in line.split():#splitting the line word by word
         
				#counting emoticons
			if ( words == ':)' or words == ':D' ):
			    	Happy += 1
			elif ( words == ':(' or words == ":'(" ):
			    	Sad += 1
		       	elif ( words == ':P' or words == ';)' ):
			    	Sarcastic += 1
		       	elif ( words == ':-o' or words == 'O_O' ):
			  	Surprised += 1
			elif ( words == 'B-)' or words == ';)' ):
			    	Crook += 1
			elif ( words == ':-/' or words == '=_=' ):
			    	Neutral += 1
			elif ( words == 'x-(' or words == '>_<' ):
			    	Angry += 1
	print"B's Emoticons are:-"
    	print"Happy = ",Happy
   	print"Sad = ",Sad
	print"Sarcastic = ",Sarcastic
    	print"Surprised = ",Surprised
    	print"Crook = ",Crook
    	print"Neutral = ",Neutral
    	print"Angry = ",Angry
	print"\n"

	#Calculation of C's Emoticons
	if line[0] == "C":
        	for words in line.split():#splitting the line word by word
          	#print(words)

				#counting emoticons
			if ( words == ':)' or words == ':D' ):
			    	Happy += 1
			elif ( words == ':(' or words == ":'(" ):
			    	Sad += 1
		       	elif ( words == ':P' or words == ';)' ):
			    	Sarcastic += 1
		       	elif ( words == ':-o' or words == 'O_O' ):
			  	Surprised += 1
			elif ( words == 'B-)' or words == ';)' ):
			    	Crook += 1
			elif ( words == ':-/' or words == '=_=' ):
			    	Neutral += 1
			elif ( words == 'x-(' or words == '>_<' ):
			    	Angry += 1
	print"C's Emoticons are:-"
    	print"Happy = ",Happy
   	print"Sad = ",Sad
	print"Sarcastic = ",Sarcastic
    	print"Surprised = ",Surprised
    	print"Crook = ",Crook
    	print"Neutral = ",Neutral
    	print"Angry = ",Angry
	print"\n"

	#Calculation of E's Emoticons
	if line[0] == "E":
        	for words in line.split():#splitting the line word by word
          	#print(words)

				#counting emoticons
			if ( words == ':)' or words == ':D' ):
			    	Happy += 1
			elif ( words == ':(' or words == ":'(" ):
			    	Sad += 1
		       	elif ( words == ':P' or words == ';)' ):
			    	Sarcastic += 1
		       	elif ( words == ':-o' or words == 'O_O' ):
			  	Surprised += 1
			elif ( words == 'B-)' or words == ';)' ):
			    	Crook += 1
			elif ( words == ':-/' or words == '=_=' ):
			    	Neutral += 1
			elif ( words == 'x-(' or words == '>_<' ):
			    	Angry += 1
	print"E's Emoticons are:-"
    	print"Happy = ",Happy
   	print"Sad = ",Sad
	print"Sarcastic = ",Sarcastic
    	print"Surprised = ",Surprised
    	print"Crook = ",Crook
    	print"Neutral = ",Neutral
    	print"Angry = ",Angry
	print"\n"
		
	#Calculation of G's Emoticons
	if line[0] == "G":
        	for words in line.split():#splitting the line word by word
          	#print(words)

				#counting emoticons
			if ( words == ':)' or words == ':D' ):
			   	Happy += 1
			elif ( words == ':(' or words == ":'(" ):
			   	Sad += 1
		       	elif ( words == ':P' or words == ';)' ):
			    	Sarcastic += 1
		       	elif ( words == ':-o' or words == 'O_O' ):
			  	Surprised += 1
			elif ( words == 'B-)' or words == ';)' ):
			    	Crook += 1
			elif ( words == ':-/' or words == '=_=' ):
			    	Neutral += 1
			elif ( words == 'x-(' or words == '>_<' ):
			    	Angry += 1
	print"G's Emoticons are:-"
    	print"Happy = ",Happy
   	print"Sad = ",Sad
	print"Sarcastic = ",Sarcastic
    	print"Surprised = ",Surprised
    	print"Crook = ",Crook
    	print"Neutral = ",Neutral
    	print"Angry = ",Angry
	print"\n"

	for words in line.split():#splitting the line word by word	
			#counting emoticons
			if ( words == ':)' or words == ':D' ):
			    	Happy += 1
			elif ( words == ':(' or words == ":'(" ):
			    	Sad += 1
		       	elif ( words == ':P' or words == ';)' ):
			    	Sarcastic += 1
		       	elif ( words == ':-o' or words == 'O_O' ):
			  	Surprised += 1
			elif ( words == 'B-)' or words == ';)' ):
			    	Crook += 1
			elif ( words == ':-/' or words == '=_=' ):
			    	Neutral += 1
			elif ( words == 'x-(' or words == '>_<' ):
			    	Angry += 1	

	
Emoticons_Sum = Happy + Sad + Sarcastic + Surprised + Crook + Neutral + Angry 	#Sum of Emoticons

#Calculating individual Emoticon's percentage
Happy = (Happy*100.0)/Emoticons_Sum		# Percentage of Happiness
Sad = (Sad*100.0)/Emoticons_Sum			# Percentage of Sadness     
Sarcastic = (Sarcastic*100.0)/Emoticons_Sum	# Percentage of Sarcasticness
Surprised = (Surprised*100.0)/Emoticons_Sum	# Percentage of Surpriseness
Crook = (Crook*100.0)/Emoticons_Sum		# Percentage of Crookness
Neutral = (Neutral*100.0)/Emoticons_Sum		# Percentage of Neutral
Angry = (Angry*100.0)/Emoticons_Sum		# Percentage of Angry

#Printing Percentage of all the Emoticons
print"Percentage of Happiness = ",Happy
print"Percentage of Sadness = ", Sad
print"Percentage of Sarcasticness = ",Sarcastic
print"Percentage of Surpriseness = ", Surprised
print"Percentage of Crookness = ", Crook
print"Percentage of Neutral = ", Neutral
print"Percentage of Angry = ", Angry
file.close()	
		
