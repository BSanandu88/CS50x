from cs50 import SQL
from sys import argv,exit
import csv

def partition_name(full_name):
	names = full_name.split()
    return names if len(name) >= 3 else [names[0],None,names[1]]

if len(argv) != 2:
	print("Incorrect number of arguments")
    exit(1)


db = SQL("sqlite:///students.db")

csv_path = argv[1]
with open(csv_path) as csv_file:
	reader = csv.DictReader(csv_file)
	for row in reader:
		names = partition_name(row["name"])
		db.execute("INSERT INTO students(first,middle,last,house,birth) VALUES(?,?,?,?,?)",names[0],names[1],names[2],row["house"],row["birth"])
		
		