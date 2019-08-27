#/env/bin/Python3
# 

### Libraries 
import os
import sys
import requests

### Insert a Token 
token = os.getenv('BREACH_TOKEN')
headers = {
  'Authorization': token
}

keys = ['email', 'records', 'isAssigned', 'breaches']
email = str(sys.argv[1])

#def request_mail(mail):
r = requests.get('https://breachreport.com/api/v1/email/{0}/check'.format(email),\
				 params={}, headers = headers).json()

for i in r.keys():
	print(r[i])
