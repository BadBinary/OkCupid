#!/usr/bin/env python

import urllib2
import json
import os
import re
from BeautifulSoup import BeautifulSoup
from baseclass import OkCupid

def getpageusernames(url):
	request = urllib2.build_opener()
	request.addheaders.append(OkCupid.cookietuple)
	returnedpage = request.open(url)
	usernamehtml = BeautifulSoup(returnedpage.read()).findAll("span", { "class" : "username" })
	finallist = []
	for i in usernamehtml:
		finallist.append(i.text.encode("utf-8"))
	return finallist

if  __name__ =='__main__':
	maindir = os.getcwd()
	queries = json.load(open('queries.json'))
	for query in queries:
		filterout = []
		for i in query['filterout']
			filterout += OkCupid.getlist(i.encode("utf-8"))
		currentlist = OkCupid.getlist(query['filepath'].encode("utf-8"))
		while True:
			print(query['name'].encode("utf-8") + ' List Count: ' + str(len(currentlist)))
			matched = []
			matchcount = 0
			#url manipulation code
			#currenturl = query['queryurl'].encode("utf-8")
			#re.sub('timekey=[0-9]', '', url)
			#&low=501&count=50
			potentials = getpageusernames(query['queryurl'].encode("utf-8"))
			for potential in potentials:
				if potential in filterout:
					continue
				else:
					matchcount += 1
					matched.append(potential)
					filterout.append(potential)
			currentlist = currentlist + matched
			currentlist.sort()
			OkCupid.writelisttofile(query['filepath'].encode("utf-8"), currentlist)
			if matchcount == 0:
				break
