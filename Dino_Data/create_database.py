import sqlite3 as sq
import csv

sci_in = open('sci_info.tsv', 'r')
sci_reader = csv.reader(sci_in, delimiter='\t')

sci_out = open('sci_info_out.csv', 'w')
sci_writer = csv.writer(sci_out)

for row in sci_reader:
	sci_writer.writerow(row)


sci_in.close()
sci_out.close()

SELECT Name_Info.Name, Sci_Info.Sci_ID, Chr.Char_ID FROM Name_Info
JOIN Dinosaur ON Name_Info.Name = Dinosaur.Name
JOIN Location ON Dinosaur.Location_ID = Location.ID
JOIN Period ON Dinosaur.Period_ID = Period.ID
JOIN Sci_Info ON Sci_Info.Taxonomy = Dinosaur.Taxonomy AND Sci_Info.Species=Dinosaur.Type_Species AND Sci_Info.Period = Period.Name AND Sci_Info.Place_Found = Location.Found
JOIN Characteristic ON Dinosaur.Characteristic_ID = Characteristic.ID
JOIN Length ON Characteristic.Length_ID = Length.ID
JOIN Chr ON Chr.Meters = Length.Meters AND Chr.Weight_kg = Characteristic.weight_kg AND Chr.Teeth = Characteristic.Teeth AND Chr.How_it_moved = Characteristic.How_it_moved AND Chr.Diet = Diet.Type
JOIN Diet ON Dinosaur.Diet_ID = Diet.ID
;
