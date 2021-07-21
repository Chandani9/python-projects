import requests
import hashlib
import sys

def requests_api_data(query_char):
	url='https://api.pwnedpasswords.com/range/'+query_char
	res=requests.get(url)
	#check if password is above 200 response or not
	if res.status_code != 200:
		raise RuntimeError(f'error fetching:{res.status_code},check the api and try again')
	return res

#this function give as how many charcter should match with sha1 algorithm by response.text
#def read_res(response):
#	print(response.text)

#actual has to check,own password check
#hash is function argv which used to store response,and hash to check denote tail(actual password)
def get_password_leaks_count(hashes,hash_to_check):
	hashes=(line.split(':') for line in hashes.text.splitlines())
	for h,count in hashes:
		#print(h,count)give number of count on hash we get
		if h == hash_to_check:
			return count#retrun how many times password leack
	return 0

#convert password to SHA1 algorithm.
def pwned_api_check(password):
	sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char=sha1password[:5]
	tail=sha1password[5:]
	response=requests_api_data(first5_char)
	#print(sha1password)
	#print(first5_char,tail)just for check that every thing is working propar or not. 
	#print(response) 
	#return read_res(response)
	return get_password_leaks_count(response,tail)

#requests_api_data('123')
#pwned_api_check('123')
#to print the result of  information
def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count :
			print(f'{password}was found {count}time.....you should probably change your password!')
		else:
			print(f'password not found,,carry on!!!')
	return 'DONE'

main(sys.argv[1:])


