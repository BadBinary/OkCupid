#!/usr/bin/env python

import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
import re
from baseclass import OkCupid

def deletethread(threadid, username, receiverid):
	didntmsgbacklist = OkCupid.getlist('./Lists/DidntMsgBack.txt')
	didntmsgbacklist.append(username)
	OkCupid.writelisttofile('./Lists/DidntMsgBack.txt', didntmsgbacklist)
	body = { 'deletethread' : 'DELETE', 'mailaction' : '3', 'buddyname' : username, 'r1' : username, 'threadid' : threadid, 'receiverid' : receiverid, 'folderid' : '2', 'body_to_forward' : ''}
	data = urllib.urlencode(body)
	delurl = 'http://www.okcupid.com/mailbox?readmsg=true&threadid=' + threadid + '&folder=2'
	delrequest = urllib2.Request(delurl, data, OkCupid.cookiedict)
	delrespon = urllib2.urlopen(delrequest)

def checkthread(threadid):
	threadurl = 'http://www.okcupid.com/messages?readmsg=true&threadid=' + threadid + '&folder=2'
	threadreq = urllib2.build_opener()
	threadreq.addheaders.append(OkCupid.cookietuple)
	returnedthreadpage = threadreq.open(threadurl)
	threadsoup = BeautifulSoup(returnedthreadpage.read())
	threadmsgs = threadsoup.findAll('div', { 'class' : 'message' })
	username = threadsoup.find('a', { 'class' : 'buddyname' }).text.encode("utf-8")
	receiverid = threadsoup.find('input', { 'name' : 'receiverid' })['value'].encode("utf-8")
	if len(threadmsgs) == 2:
		deletethread(threadid, username, receiverid)

if  __name__ =='__main__':
	pagecount = 1
	while True:
		request = urllib2.build_opener()
		request.addheaders.append(OkCupid.cookietuple)
		sentmessagespage = request.open('http://www.okcupid.com/messages?low=' + str(pagecount) + '&folder=2')
		soup = BeautifulSoup(sentmessagespage.read())
		msghtml = soup.findAll('li', { 'class' : re.compile('^readMessage') })
		if len(msghtml) == 0:
			break
		for thread in msghtml:
			checkthread(thread['id'].encode('utf-8').replace('message_', ''))
		pagecount += 30
