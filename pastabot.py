#!/usr/bin/python
import praw
import re
import sys
import time
import os.path
import random
import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
import colorama
from colorama import Fore, Back, Style

colorama.init()
colors = list(vars(colorama.Fore).values())

pastafile = "collection.pasta"
IDfile = "pasta_ids.pasta"

def collectPasta(pasta, collected_pasta):
	if (len(pasta) > 5):
		collected_pasta.append(pasta)
		with open(pastafile, "w") as f:
			for pasta in collected_pasta:
				f.write(pasta + "\n$------------------$\n")

def collectPastaID(pasta_id, id_list):
	id_list.append(pasta_id)
	with open(IDfile, "w") as f:
		for pasta_id in id_list:
			f.write(pasta_id + "\n")

def randompasta():
	with open(pastafile, "r") as f:
	   pastalist = f.read()
	   pastalist = pastalist.split("$------------------$")
	   pastalist = list(filter(None, pastalist))
	pasta = random.choice(pastalist)
	return pasta
	
def login(): 
	r = praw.Reddit('emojipastabot')
	return r
	
		
def run(r):
		subreddit = r.subreddit("pcmasterrace")
		try:	
			print("Crawling through:" , subreddit)
			#Creates a file for storing pastas if it doesn't exist
			#Imports collected pasta as a list	
			if not os.path.isfile(pastafile):
				collected_pasta = []
			else:
				with open(pastafile, "r") as f:
				   collected_pasta = f.read()
				   collected_pasta = collected_pasta.split("$------------------$")
				   collected_pasta = list(filter(None, collected_pasta))
				
		#Creates a file to store ids if one does not exist
		#Imports IDs as a list
			if not os.path.isfile(IDfile):
				pasta_ids = []
			else:
				with open(IDfile, "r") as f:
				   pasta_ids = f.read()
				   pasta_ids = pasta_ids.split("\n")
				   pasta_ids = list(filter(None, pasta_ids))
			
			for submission in subreddit.hot(limit = 1000):
				if submission.id not in pasta_ids:
					
					
					print(random.choice(colors)+"Pasta:", submission.title, "Id:", submission.id)
					
					collectPasta( submission.selftext, collected_pasta)
					
					collectPastaID(submission.id, pasta_ids)
					time.sleep(1)
		except AttributeError:
			pass
			
def main():
	r = login()
	run(r)
	
	print("Here's a random pasta. Enjoy! \n", randompasta())
	
main()