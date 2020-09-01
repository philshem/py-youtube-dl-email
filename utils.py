import os
from dotenv import load_dotenv

# https://murhabazi.com/read-emails-python/

def read_credentails():
	"""
	Return user’s credentials from the environment variables file and 
	raise a an exception if the credentials are not present 
	
	Raises:
		NotImplementedError: [description]
	"""
	load_dotenv()

	USER_EMAIL = os.getenv("USER_EMAIL")
	USER_PASSWORD = os.getenv("USER_PASSWORD")
	USER_IMAP = os.getenv("USER_IMAP")

	if USER_IMAP and USER_EMAIL and USER_PASSWORD:
		return USER_IMAP, USER_EMAIL, USER_PASSWORD
	else:
		raise ValueError('Please add a .env file and write the credentials it it. See .env_sample for an example.')