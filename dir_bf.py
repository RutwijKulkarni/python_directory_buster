#! /usr/bin/python
'''*****************************************************--USAGE--****************************************************************
$ python dir_bf.py <URI/IP> <WORDLIST> <OUTPUT>

where	URL= A fully qualified server name/IP (e.g. www.gmu.edu, x.x.x.x)
		WORDLIST= A file that will contain the names of directories to be bruteforced (e.g. wordlist.txt)
		OUTPUT= A file that will store the successful directory names (e.g. output.txt)
		
$ python dir_bf.py hackthis.co.uk directory-list-2.3-small.txt output.txt
******************************************************************************************************************************'''

print '\n\t\t[Author] Rutwij Kulkarni [rkulkar6 at gmu dot edu]\n' + '\t\t[Version] 1.0\n'

try:
	import sys
	import requests
	count404=0									#A variable to keep a count of directories that return status code of [404 NOT FOUND]
	
	rhost = sys.argv[1]							#Accept URL/IP from User
	wordlist = sys.argv[2]						#Accept Wordlist from User (contains directory names)
	output=sys.argv[3]							#Specify the Output file to which the program output will be written
	
	print '\n[START]'
	print '\nConnecting to [%s] . . . please wait' % (rhost)	#Checking whether the host is up or down
	try:
		response = requests.get('http://' + rhost).status_code				
		if response==200:										
			print '\nResponse: %d  Connected to %s' %(response, rhost)
	except:
		print '\nConnection to %s failed!' %(rhost)
		sys.exit(1)
	
	try:
		with open(wordlist) as file:
			directories = file.read().strip().split('\n')
				
	except IOError:
		print '\nFailed to read "%s"' %(wordlist)
		print 'Please verify the file name\n'
		sys.exit(1)
	
	def brute_force(directory):
		try:
			#print 'Trying %s/%s/' %(rhost,directory)
			dir_response = requests.get('http://'+rhost+'/'+ directory+'/').status_code	
			
		except Exception:
			print '\nError'
			sys.exit(1)
		
		def OK():														#200 OK
			print '\nResponse: %d %s/%s/' %(dir_response,rhost,directory)
			with open(output,'a') as file2:
				file2.write('/'+directory+'/')
				file2.write("\n")
		
		def NOT_FOUND():												#404 NOT FOUND
			global count404								
			count404=count404+1
			#print '\n%d - NOT FOUND %s/%s' %(response,rhost,directory)
			#print 'Count= %d' %(count404)		
			
		
		def NO_CONTENT():												#204 NO CONTENT
			#print '\nListing directory names having Status code 204 '
			print '\nResponse: %d %s/%s/' %(dir_response,rhost,directory)
			'''with open(output,'a') as file2:
				file2.write('/'+directory+'/')
				file2.write("\n")'''
				
		
		def MOVED_PERMANENTLY():										#301 MOVED PERMANANETLY
			#print '\nListing directory names having Status Code 301 '
			print '\nResponse: %d %s/%s/' %(dir_response,rhost,directory)
			'''with open(output,'a') as file2:
				file2.write('/'+directory)
				file2.write("\n")'''
		
		def FOUND():													#302 FOUND
			#print '\nListing directory names having Status code 302 '
			print '\nResponse: %d %s/%s/' %(dir_response,rhost,directory)
		
		def TEMPORARY_REDIRECT():										#307 TEMPORARY REDIRECT
			#print '\nListing directory names having Status code 307 '
			print '\n%Response: %d %s/%s/' %(dir_response,rhost,directory)
		
		def FORBIDDEN():												#403 FORBIDDEN
			#print '\nListing directory names having Status code 403 '
			print '\nResponse: %d %s/%s/' %(dir_response, rhost,directory)	
		
				
		status_codes =	{												#Defining the dictionary
							200: OK,
						 	204: NO_CONTENT,
						 	301: MOVED_PERMANENTLY,
						 	302: FOUND,
						 	307: TEMPORARY_REDIRECT,
						 	403: FORBIDDEN,
						 	404: NOT_FOUND,
						}
						
		if dir_response == 200:
			status_codes[dir_response]()
			
		if dir_response == 204:
			status_codes[dir_response]()
		
		if dir_response == 301:
			status_codes[dir_response]()
		
		if dir_response == 302:
			status_codes[dir_response]()
		
		if dir_response == 307:
			status_codes[dir_response]()
		
		if dir_response == 403:
			status_codes[dir_response]()
			
		if dir_response == 404:
			status_codes[dir_response]()
	
	for directory in directories:
		brute_force(directory)
	print '\n[FINISHED]'
	
except:
	sys.exit(1)
'''SCRIPT END'''		