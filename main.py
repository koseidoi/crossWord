import random

size = 8
tryTimes = 10
cheeze = 1

def conformData():	
	with open("info.txt") as f:
		element = f.read()
	elements = element.split("\n")

	size = 8

	dictionary = {}

	for i in elements:
		for j in i:
			dictionary.update({j:element.count(j)})

	dictionary = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)

	chars = {}

	for i in elements:
		score = 0
		for j in dictionary:
			if j[0] in i:
				score += j[1]
		chars.update({i:score})

	chars = sorted(chars.items(), key=lambda x:x[1], reverse=True)

	print(chars)
	return chars


tile = []
def makeTiles():
	for i in range(size):
		part = []
		for j in range(size):
			part.append("  ")
		tile.append(part)
		
def paintTiles():
	for i in tile:
		print(i)
		print()

def findCommon(char):
	rightPlaces = []
	for y,ti in enumerate(tile):
		for x,u in enumerate(ti):
			if char == u:
				rightPlaces.append([x,y])
	if(len(rightPlaces) == 0):
		return "None","None"
	else:
		rightPlace = random.choice(rightPlaces)
		return rightPlace[0],rightPlace[1]

def checkDouble(char,x,y,num,tilt):
	if tilt == "line":
		for times,ch in enumerate(char):
			if tile[y-num+times][x] == "  " or tile[y-num+times][x] == ch:
				None
			else:
				return False
		return True
	else:
		for times,ch in enumerate(char):
			if tile[y][x-num+times] == "  " or tile[y][x-num+times] == ch:
				None
			else:
				return False
		return True

def reload(list):
	global cheeze
	cheeze += 1
	if list[4] == "line":
		for times,ch in enumerate(list[0]):
			tile[list[2]-list[3]+times][list[1]] = ch
	else:
		for times,ch in enumerate(list[0]):
			tile[list[2]][list[1]-list[3]+times] = ch

leftWords = []
def moreThan2(char,tilt):
	ava = []
	for num,ch in enumerate(char):
		x,y = findCommon(ch)
		if x == "None":
			None
		elif tilt == "line":
			if size >= y + len(char) - num and y - num >= 0 and checkDouble(char,x,y,num,"line"):
				ava.append([char,x,y,num,"line"])
		elif tilt == "row":
			if size >= x + len(char) - num and x - num >= 0 and checkDouble(char,x,y,num,"row"):
				ava.append([char,x,y,num,"row"])

	av = []
	if ava == []:
		leftWords.append(char)
	else:
		av = random.choice(ava)
		reload(av)

def extra2(char,tilt,flag):
	ava = []
	for num,ch in enumerate(char):
		x,y = findCommon(ch)
		if x == "None":
			None
		elif tilt == "line":
			if size >= y + len(char) - num and y - num >= 0 and checkDouble(char,x,y,num,"line"):
				ava.append([char,x,y,num,"line"])
		elif tilt == "row":
			if size >= x + len(char) - num and x - num >= 0 and checkDouble(char,x,y,num,"row"):
				ava.append([char,x,y,num,"row"])

	av = []
	if ava == []:
		None
	else:
		if flag:
			leftWords.remove(char)
		av = random.choice(ava)
		reload(av)
		

			
def theOne(i):
	int = random.randint(0,3)
	if int == 0:		
		for j in range(len(i[0])):
			tile[j][3] = i[0][j]
		tilt = "line"
	if int == 1:
		for j in range(len(i[0])):
			tile[j][4] = i[0][j]
		tilt = "line"
	if int == 2:
		for j in range(len(i[0])):
			tile[3][j] = i[0][j]
	if int == 3:
		for j in range(len(i[0])):
			tile[4][j] = i[0][j]
	
def exe():
	times = 0
	tilt = "row"
	for i in chars:
		if times == 0:
			theOne(i)
		else:
			moreThan2(i[0],tilt)

		if tilt == "row":
			tilt = "line"
		elif tilt == "line":
			tilt = "row"
		
		if times != 0:
			moreThan2(i[0],tilt)

		times += 1

	tilt = "row"
	for _ in range(tryTimes):
		for word in leftWords:
			extra2(word,tilt,False)

			if tilt == "row":
				tilt = "line"
			elif tilt == "line":
				tilt = "row"
						
			extra2(word,tilt,True)


	print(leftWords)


if __name__ == "__main__":
	chars = conformData()
	makeTiles()
	exe()
	paintTiles()
	print(cheeze)
