# https://github.com/ytdl-org/youtube-dl
# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl
# requires youtube-dl on your path. instructions: https://github.com/ytdl-org/youtube-dl#installation
# requires ffmpeg

from youtube_dl import YoutubeDL
import os

'''
takes list of youtube urls and downloads mp3s to the specified folder
'''

import youtube_dl

def download_mp3(url_list, download_folder='mp3'):
	ydl = YoutubeDL()

	ydl_opts = {
		'quiet' : True,
		'no_warnings' : True,
		'verbose' : False,
		'ignoreerrors':True,
		#'verbosity': 'no_warnings',
		'format': 'bestaudio/best',
		'default_search': 'fixup_error',
		'outtmpl': download_folder + os.sep + '%(title)s' + '.mp3',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
	}
	
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		## actually, the download() function can accept a list.
		## but then I lost error handling for indivual urls
		## and the entire script would crash when one url was invalid

		ydl.download(url_list)
		
		# so now it's one by one
		#for url in url_list:
		#	try:
		#		ydl.download(url_list)
		#	except youtube_dl.utils.DownloadError:
		#		print('Invalid URL:',url)
		#		#print(youtube_dl.utils.DownloadError)
		#		continue




#url_list = ['https://youtu.be/rBu0BRTx2x8']
#download_mp3(url_list)