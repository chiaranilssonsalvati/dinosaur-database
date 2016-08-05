import sqlite3
import csv
import wikipedia as w
import random

conn = sqlite3.connect('Dino_Data/Dino.db')
c = conn.cursor()


def choice1():
	x = list(c.execute("SELECT Sci_Info.Place_Found, Chr.Diet, ID_Info.Name FROM Sci_Info JOIN ID_Info ON Sci_Info.Sci_ID=ID_Info.Sci_ID JOIN Chr ON ID_Info.Char_ID=Chr.Char_ID"))
	y = x[random.randint(0, len(x)-1)]
	rowASCII = []
	for item in y:
		if type(item) == type(u'hi'):
			rowASCII.append(item.encode('ascii'))
		else:
			rowASCII.append(item)
	print("The dinosaur "+rowASCII[2]+" was "+rowASCII[1]+" and lived in "+rowASCII[0]+".")
	menu()

def choice2():
	x = list(c.execute("SELECT Sci_Info.Period, Chr.How_It_Moved, ID_Info.Name FROM Sci_Info JOIN ID_Info ON Sci_Info.Sci_ID=ID_Info.Sci_ID JOIN Chr ON ID_Info.Char_ID=Chr.Char_ID"))
	y = x[random.randint(0, len(x)-1)]
	rowASCII = []
	for item in y:
		if type(item) == type(u'hi'):
			rowASCII.append(item.encode('ascii'))
		else:
			rowASCII.append(item)
	print("The dinosaur "+rowASCII[2]+" lived in the "+rowASCII[0]+" period and moved "+rowASCII[1]+".")
	menu()


def choice3():
	x = list(c.execute("SELECT Diet, Avg(Weight_kg) FROM Chr GROUP BY Diet"))
	herbivorous = x[1]
	carnivorous = x[0]
	omnivorous = x[3]
	# for item in herbivorous, carnivorous, omnivorous:
	# 	if type(item) == type(u'hi'):
	# 		rowASCII.append(item.encode('ascii'))
	# 	else:
	# 		rowASCII.append(item)
	print("With an average weight of "+str(herbivorous[1])+" kgs, "+herbivorous[0].encode('ascii')+" dinosaurs were the heaviest, followed by "+carnivorous[0].encode('ascii')+" dinosaurs, at "+str(carnivorous[1])+" kgs on average, and "+omnivorous[0].encode('ascii')+" dinosaurs at an average of "+str(omnivorous[1])+" kgs.")
	menu()

def choice4():
	x = list(c.execute("SELECT * FROM Name_Info"))
	y = x[random.randint(0, len(x)-1)]
	rowASCII = []
	for item in y:
		if type(item) == type(u'hi'):
			rowASCII.append(item.encode('ascii'))
		else:
			rowASCII.append(item)
	print("The dinosaur "+rowASCII[0]+", whose name is pronounced "+rowASCII[1]+", means "+rowASCII[2]+".  The "+rowASCII[0]+" was named by "+rowASCII[3]+" in the year "+rowASCII[4]+".")
	# s = u'\U0001f63b'
	# print(s)
	menu()


def queries(choice):
	if choice == '1':
		choice1()
	elif choice == '2':
		choice2()
	elif choice == '3':
		choice3()
	elif choice == '4':
		choice4()
	elif choice != 'quit':
		errormessage()
	else:
		menu()

def errormessage():
	print("Error- please choose 1, 2, 3, 4, or quit. ")
	menu()



def welcome():
	a = u'\U0001F432'
	b = u'\U0001F409'
	print("\nWelcome to the Dino Den!\n")
	print(w.summary("Dinosaur", sentences=4))
	print("\nOn this site, you will be able to learn about the lives of many different dinosaurs. \n")
	print(a +"    " +b)
	menu()

def menu():
	a = u'\U0001F30E'
	b = u'\U0001F6B6'
	c = u'\U0001F3C3'
	d = u'\U0001F357'
	e = u'\U0001F33F'
	f = u'\U0001F4AC'
	print('''You can choose to:
	1. Learn about how a dinosaur's location relates to its diet. %s
	2. Learn about how the period when a dinosaur lived related to how it moved. %s  %s
	3. Learn about how their diets related to their weights. %s  %s
	4. Learn about the etymology of a dinosaur's name. %s
	''' % (a, b, c, d, e, f))
	choice = raw_input("Choose 1, 2, 3, or 4, or 'quit' to quit. ").lower()
	if choice != 'quit':
		queries(choice)
	else:
		s = u'\U0001F44B'
		print("Thank you for visiting the Dino Den.  Goodbye! "+s)



welcome()