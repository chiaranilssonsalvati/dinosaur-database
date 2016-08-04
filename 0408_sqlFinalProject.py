import sqlite3
import csv
import wikipedia as w
import random

conn = sqlite3.connect('Dino_Data/Dino.db')
c = conn.cursor()




def choice1():
	x = list(c.execute("SELECT Sci_Info.Place_Found, Chr.Diet, ID_Info.Name FROM Sci_Info JOIN ID_Info ON Sci_Info.Sci_ID=ID_Info.Sci_ID JOIN Chr ON ID_Info.Char_ID=Chr.Char_ID"))
	y = x[random.randint(0, len(x))]
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
	y = x[random.randint(0, len(x))]
	rowASCII = []
	for item in y:
		if type(item) == type(u'hi'):
			rowASCII.append(item.encode('ascii'))
		else:
			rowASCII.append(item)
	print("The dinosaur "+rowASCII[2]+" lived in the "+rowASCII[0]+" period and moved "+rowASCII[1]+".")
	menu()


def choice3():
	print('hi')
	menu()



def queries(choice):
	if choice == '1':
		choice1()
	elif choice == '2':
		choice2()
	elif choice == '3':
		choice3()
	elif choice != 'quit':
		errormessage()
	else:
		menu()

def errormessage():
	print("Error- please choose 1, 2, 3, or quit. ")
	menu()



def welcome():
	print("\nWelcome to the Dino Den!\n")
	print(w.summary("Dinosaur", sentences=4))
	print("\nOn this site, you will be able to learn about the lives of many different dinosaurs. \n")
	menu()

def menu():
	print('''You can choose to:
	1. Learn about how a dinosaur's location relates to its diet.
	2. Learn about how the period when a dinosaur lived related to how it moved.
	3. tbd
	''')
	choice = raw_input("Choose 1, 2, or 3, or 'quit' to quit. ").lower()
	if choice != 'quit':
		queries(choice)



welcome()