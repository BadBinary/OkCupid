from baseclass import OkCupid

if  __name__ =='__main__':
	sentmsgs = OkCupid.getlist("./Lists/SentAMessage.txt") + OkCupid.getlist("./Lists/AlreadyMessagedBack.txt")
	fivestar = OkCupid.getlist("./Lists/HottieList.txt")
	fourstar = OkCupid.getlist("./Lists/FourStarList.txt")
	threestar = OkCupid.getlist("./Lists/ThreeStarList.txt")

	for i in fivestar:
		if i in sentmsgs:
			fivestar.remove(i)
			continue
		if i in fourstar:
			fourstar.remove(i)
		if i in threestar:
			threestar.remove(i)

	for j in fourstar:
		if j in sentmsgs:
			fourstar.remove(j)
			continue
		if j in threestar:
			threestar.remove(j)

	for k in threestar:
		if k in sentmsgs:
			threestar.remove(k)

	OkCupid.writelisttofile("./Lists/HottieList.txt", fivestar)
	OkCupid.writelisttofile("./Lists/FourStarList.txt", fourstar)
	OkCupid.writelisttofile("./Lists/ThreeStarList.txt", threestar)