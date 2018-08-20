import sys


def main():
	be850, bec = loadfiles()
	startscreen()
	text = getinput()
	beclist, neither = compare(text, be850, bec)
	endscreen(beclist, neither)

def loadfiles():
	try:
		WordsFile = open("be850.txt", "r")
		for Word in WordsFile:
			be850 = Word.split()
		WordsFile.close()
	except FileNotFoundError:
		print("A file is missing, please make sure you have all files downloaded.", file=sys.stderr)
		exit()

	try:
		WordsFile = open("bec.txt", "r")
		for Word in WordsFile:
			bec = Word.split()
		WordsFile.close()
	except FileNotFoundError:
		print("A file is missing, please make sure you have all files downloaded.", file=sys.stderr)
		exit()
	return be850, bec



def startscreen():
	print("++++++++++++++++++++++++++++++++++++++++")
	print("+               Welcome!               +")
	print("+ This tool can be used to make sure   +")
	print("+ texts are written in Simple English. +")
	print("++++++++++++++++++++++++++++++++++++++++")

def getinput():
	text = str(input("Please input the text that should be tested...  "))
	text = text.split()
	return text

def compare(text, be850, bec):
	beclist = []
	neither = []
	for word in text:
		if not checkwordisvalid(word, be850):
			if checkwordisvalid(word, bec):
				beclist.append(word)
			else: 
				neither.append(word)
	return beclist, neither


#def checkwordisvalid(word, wordlist):
#	print (word.upper())
#	ValidWord = False
#	First = 0
#	Last = len(wordlist) - 1
#	while First <= Last and not ValidWord:
#		Midpoint = (First + Last)//2
#		print (wordlist[First])
#		print(wordlist[Midpoint])
#		print (wordlist[Last])
#		if wordlist[Midpoint] == word:
#			ValidWord = True
#		else:
#			if wordlist[Midpoint] < word:
#				First = Midpoint + 1
#			else:
#				Last = Midpoint - 1
#	print (ValidWord)
#	return ValidWord

def checkwordisvalid(word, wordlist):
	for item in wordlist:
		if word == item:
			return True
	return False

def endscreen(beclist, neither):
	print("++++++++++++++++++++++++++++++++++++++++")
	print()
	print(len(beclist), "words used are not in the 850 words allowed in Basic English. These are: ")
	for item in beclist:
		print(item)
	print(len(neither), "words used are also not in an extended list of common words. These are: ")
	for item in neither:
		print(item)

if __name__ == '__main__':
	main()
