import requests 

count = 0

c = 0

while count < 2600: #total iPads in the school
 	c = str(int(c)+1) #add one from last iPad ID updated 
	url = 'http://media.fairfieldprep.org:5000/update/' #URL of the JSS update utility with /update endpoint
	r = requests.get(url + c) 
	print(r.json) #200 Means established connection and recieved update request
	print(count) #prints iPad number just updated
	count += 1
