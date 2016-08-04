import sqlite3
import csv
import wikipedia as w


conn = sqlite3.connect('Dino.db')
c = conn.cursor()




def choice1():
	c.execute("SELECT Sci_Info.Place_Found, Chr.Diet FROM Sci_Info JOIN Dinosaur ON Sci_Info.Sci_ID=Dinosaur.Sci_ID JOIN Chr ON Dinosaur.Char_ID=Chr.Char_ID")

def choice2():
	c.execute("SELECT Sci_Info.Period, Chr.How_It_Moved FROM Sci_Info JOIN Dinosaur ON Sci_Info.Sci_ID=Dinosaur.Sci_ID JOIN Chr ON Dinosaur.Char_ID=Chr.Char_ID")


def choice3():
	




def queries(choice):
	if choice == '1':
		choice1()
	elif choice == '2':
		choice2()
	elif choice == '3':
		choice3()
	else:
		print("Error- please choose 1,2, or 3.")





def menu():
	print("\nWelcome to the Dino Den!\n")
	print(w.summary("Dinosaur", sentences=4))
	print("\nOn this site, you will be able to learn about the lives of many different dinosaurs. You can choose to \n")
	choice = raw_input("Choose 'quit' to quit." ).upper()
	while choice != 'QUIT':
		queries(choice)



menu()





