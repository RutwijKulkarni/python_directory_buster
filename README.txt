******************************************************************************************************************************
Author: Rutwij Kulkarni
Name of script: dir_bf.py
Date: 09/15/2017
Script Version: 1.0
Language Version: Python 2.7.10
GEORGE MASON UNIVERSITY

INTRO: This script will brute force directories (at level 1)[directory names from the given wordlist] on a particular given 
URI/IP.
  
*****************************************************--USAGE--****************************************************************
$ python dir_bf.py <URI/IP> <WORDLIST> <OUTPUT>

where	URL= A fully qualified server name/IP (e.g. www.gmu.edu, x.x.x.x)
		WORDLIST= A file that will contain the names of directories to be bruteforced (e.g. wordlist.txt)
		OUTPUT= A file that will store the successful directory names (e.g. output.txt)
		
$ python dir_bf.py hackthis.co.uk directory-list-2.3-small.txt output.txt
******************************************************************************************************************************

*****************************************************--REFERENCES--***********************************************************
[1] https://null-byte.wonderhowto.com/how-to/build-directory-brute-forcing-tool-python-0169477/
[2] http://www.tutorialspoint.com/python/python_files_io.htm 
[3] http://www.dummies.com/programming/python/how-to-replace-the-switch-statement-with-a-dictionary-in-python/
******************************************************************************************************************************

The script dir_bf.py can definitely be used in future classes. The script can be modified to recursively brute force directories.				