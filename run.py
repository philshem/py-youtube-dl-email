
import utils
import parse_email
import download_mp3

def main():

	download_path = 'mp3s'
	domain_whitelist = ['youtube.com','youtu.be']
	
	imap,user,pw = utils.read_credentails()

	html = parse_email.parse_email(imap,user,pw)

	url_list = parse_email.parse_urls(html)

	print('all urls:',url_list)

	valid_urls = parse_email.validate_urls(url_list, domain_whitelist)

	print('valid urls:',valid_urls)

	# try to download, except is in function
	download_mp3.download_mp3(valid_urls,download_path)

if __name__ == "__main__":
	main()