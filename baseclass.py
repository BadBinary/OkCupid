import urllib
import urllib2
import getpass
import cookielib
import requests
import json

class OkCupid(object):

	@staticmethod
	def writelisttofile(filepath, list):
		new = open(filepath, 'w')
		for item in list:
  			print >> new, item
  		new.close()

  	@staticmethod 
	def getlist(filepath):
		newfile = open(filepath, 'U')
		return newfile.read().splitlines()

	@staticmethod
	def writejson(filepath, json):
		new = open(filepath, 'w')
		new.writelines(json)
		new.close()

	@staticmethod
	def loadcookie(filepath):
		try:
   			with open(filepath):
   				pass
		except IOError:
			OkCupid.login()
		cookiefile = open(filepath, 'r')
		cookiestring = json.loads(cookiefile.read())
		if (json.loads(test).keys()[0] == 'authlink') & (json.loads(test).keys()[1] == 'session'):
			values = "session=" + cookiestring['session'].encode('utf-8') + "; authlink=" + cookiestring['authlink'].encode('utf-8')
			OkCupid.cookietuple = ('Cookie', values)
			OkCupid.cookiedict = {'Cookie' : values}
		else:
			OkCupid.login()

	@staticmethod
	def login():
		username = raw_input('Please enter your OKcupid username: ')
		password = getpass.getpass()
		loginurl = 'https://www.okcupid.com/login'
		cookiejar = cookielib.CookieJar()
		loginopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
		parameters = urllib.urlencode({'username' :  username, 'password' : password, 'dest' : '/?'})
		loginrespon = loginopener.open(loginurl, parameters)
		if 'guest' in requests.utils.dict_from_cookiejar(cookiejar).keys():
			print "Login error re-enter your login creds"
			OkCupid.login()
		cookiejson = json.dumps(requests.utils.dict_from_cookiejar(cookiejar))
		OkCupid.writejson('cookie.json', cookiejson)
		OkCupid.loadcookie('cookie.json')

OkCupid.loadcookie('cookie.json')